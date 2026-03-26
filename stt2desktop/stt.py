import logging
import subprocess
import threading
from concurrent.futures import Future, ThreadPoolExecutor

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
from rich import print

from stt2desktop.constants import IS_WAYLAND
from stt2desktop.get_bin import get_wtype_bin, get_xdotool_bin


logger = logging.getLogger(__name__)


def load_whisper_model(*, model_size: str, device: str, compute_type: str, num_workers: int) -> WhisperModel:
    print(f'Loading model {model_size} ({device=} {compute_type=} {num_workers=})...')
    model = WhisperModel(model_size, device=device, compute_type=compute_type, num_workers=num_workers)
    print('[green]Model loaded.[/green]')
    return model


def transcribe(model: WhisperModel, audio: np.ndarray) -> str:
    if len(audio) == 0:
        return ''
    logger.debug('Transcribing %d samples', len(audio))
    segments, _ = model.transcribe(audio, beam_size=5)
    result = ' '.join(seg.text for seg in segments).strip()
    logger.debug('Transcription: %r', result)
    return result


def record_until_event(*, stop_event: threading.Event, sample_rate: int) -> np.ndarray:
    """Record from the default microphone until stop_event is set."""
    chunks: list[np.ndarray] = []

    def callback(indata, frames, time, status):
        if status:
            logger.warning('Audio input status: %r', status)
        chunks.append(indata.copy())

    logger.debug('Recording started')
    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32', callback=callback):
        stop_event.wait()
    logger.debug('Recording stopped, got %d chunks', len(chunks))

    if not chunks:
        return np.array([], dtype='float32')
    return np.concatenate(chunks, axis=0).flatten()


def inject_text(text: str) -> None:
    """Inject text at the current cursor position."""
    if IS_WAYLAND:
        # wtype types text directly into the focused window
        wtype_bin = get_wtype_bin()
        subprocess.run((wtype_bin, '--', text), check=True)
    else:
        # xdotool types text by simulating key events
        xdotool_bin = get_xdotool_bin()
        subprocess.run(
            (xdotool_bin, 'type', '--clearmodifiers', '--delay', '0', '--', text),
            check=True,
        )


def record_and_inject(
    *,
    model: WhisperModel,
    stop_event: threading.Event,
    sample_rate: int,
) -> None:
    audio = record_until_event(stop_event=stop_event, sample_rate=sample_rate)
    print('[cyan]Transcribing...[/cyan]')
    text = transcribe(model, audio)
    if text:
        print(f'[green]Inserting:[/green] {text}')
        inject_text(text)
    else:
        print('[dim]No speech detected.[/dim]')


class Recorder:
    def __init__(self, *, model: WhisperModel, sample_rate: int):
        self._model = model
        self._sample_rate = sample_rate
        self._stop_event: threading.Event | None = None
        self._future: Future | None = None
        self._executor = ThreadPoolExecutor(max_workers=1)

    def start(self):
        if self._future and not self._future.done():
            return
        self._stop_event = threading.Event()
        self._future = self._executor.submit(
            record_and_inject,
            model=self._model,
            stop_event=self._stop_event,
            sample_rate=self._sample_rate,
        )
        print('[yellow]Recording...[/yellow]')

    def stop(self):
        if self._stop_event is not None:
            self._stop_event.set()
