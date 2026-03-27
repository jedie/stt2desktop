import logging
from typing import Annotated

import tyro
from cli_base.cli_tools.verbosity import setup_logging
from cli_base.tyro_commands import TyroVerbosityArgType
from pynput import keyboard
from rich import print

from stt2desktop.cli_app import app
from stt2desktop.constants import (
    DEFAULT_HOTKEY,
    DEFAULT_SAMPLE_RATE,
    DEFAULT_WHISPER_COMPUTE_TYPE,
    DEFAULT_WHISPER_DEVICE,
    DEFAULT_WHISPER_MODEL,
    DEFAULT_WHISPER_NUM_WORKERS,
    IS_WAYLAND,
    WhisperModel,
)
from stt2desktop.get_bin import get_wtype_bin, get_xdotool_bin
from stt2desktop.stt import Recorder, load_whisper_model


logger = logging.getLogger(__name__)


@app.command
def listen(
    verbosity: TyroVerbosityArgType,
    model: Annotated[
        WhisperModel, tyro.conf.arg(help='Whisper model to use for transcription.')
    ] = DEFAULT_WHISPER_MODEL,
    hotkey: Annotated[
        keyboard.Key,
        tyro.conf.arg(help='Key to hold for recording. Release to transcribe and insert text.'),
    ] = DEFAULT_HOTKEY,
    sample_rate: Annotated[
        int, tyro.conf.arg(help='Audio sample rate in Hz. Whisper expects 16000.')
    ] = DEFAULT_SAMPLE_RATE,
    device: Annotated[
        str, tyro.conf.arg(help='Device to run inference on, e.g. cpu or cuda.')
    ] = DEFAULT_WHISPER_DEVICE,
    compute_type: Annotated[
        str, tyro.conf.arg(help='Quantization type, e.g. int8, float16, float32.')
    ] = DEFAULT_WHISPER_COMPUTE_TYPE,
    num_workers: Annotated[
        int | None,
        tyro.conf.arg(help='Number of parallel transcription workers. Defaults to CPU count.'),
    ] = None,
):
    """Start the STT listener. Hold the hotkey to record, release to transcribe and insert."""

    # FIXME: Resolve here instead of in the signature so the help text shows None rather than a
    #        machine-specific CPU count, keeping it stable across platforms (CI run):
    num_workers = num_workers or DEFAULT_WHISPER_NUM_WORKERS

    setup_logging(verbosity=verbosity)

    # Before start, check if needed binaries are available:
    if IS_WAYLAND:
        get_wtype_bin()
    else:
        get_xdotool_bin()

    model = load_whisper_model(
        model_size=model,
        device=device,
        compute_type=compute_type,
        num_workers=num_workers,
    )
    recorder = Recorder(model=model, sample_rate=sample_rate)

    def on_press(key):
        if key == hotkey:
            recorder.start()

    def on_release(key):
        if key == hotkey:
            recorder.stop()

    print(f'Ready. Hold [bold]{hotkey.name}[/bold] to record, release to transcribe.')
    print('Press Ctrl+C to exit.')
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('\nExiting...')
    finally:
        recorder.stop()
