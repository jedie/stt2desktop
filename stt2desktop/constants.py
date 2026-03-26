import os
from enum import StrEnum
from pathlib import Path

from faster_whisper.utils import available_models
from pynput import keyboard

import stt2desktop


CLI_EPILOG = 'Project Homepage: https://github.com/jedie/stt2desktop'

BASE_PATH = Path(stt2desktop.__file__).parent

IS_WAYLAND = bool(os.environ.get('WAYLAND_DISPLAY'))

WhisperModel = StrEnum(
    'WhisperModel',
    [(m.replace('-', '_').replace('.', '_'), m) for m in available_models()],
)

# Default values used in the CLI
DEFAULT_WHISPER_MODEL = WhisperModel.small
DEFAULT_WHISPER_DEVICE = 'auto'  # Let faster-whisper decide the best device
DEFAULT_WHISPER_COMPUTE_TYPE = 'int8'
DEFAULT_WHISPER_NUM_WORKERS = os.cpu_count() or 1
DEFAULT_SAMPLE_RATE = 16000
DEFAULT_HOTKEY = keyboard.Key.scroll_lock
