# stt2desktop

[![tests](https://github.com/jedie/stt2desktop/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/jedie/stt2desktop/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/stt2desktop/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/stt2desktop)
[![stt2desktop @ PyPi](https://img.shields.io/pypi/v/stt2desktop?label=stt2desktop%20%40%20PyPi)](https://pypi.org/project/stt2desktop/)
[![Python Versions](https://img.shields.io/pypi/pyversions/stt2desktop)](https://github.com/jedie/stt2desktop/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/stt2desktop)](https://github.com/jedie/stt2desktop/blob/main/LICENSE)

Local speech-to-text for desktop using [faster-whisper](https://github.com/SYSTRAN/faster-whisper).

Let's you dictate text into any application without sending audio to any cloud services.
Everything runs locally on your machine — no internet connection required after the initial model was download.

Currently only tested under Linux with KDE ;)

## How it works

1. Run `./cli.py listen` (Whisper model downloaded on first run, cached on disk)
2. Hold **Scroll Lock** to record from your microphone
3. Release **Scroll Lock** — the audio is transcribed locally by faster-whisper
4. The text is typed into the focused window via `wtype` (Wayland) or `xdotool` (X11)

## Install via pipx

Requirements: Python 3.12+, a working microphone, and either `wtype` (Wayland) or `xdotool` (X11):

```bash
sudo apt install wtype     # Wayland
sudo apt install xdotool   # X11
```

You can install "stt2desktop" with [pipx](https://pipx.pypa.io/):

```bash
sudo apt install pipx
pipx install stt2desktop
```

Then run:

```bash
stt2desktop listen
```

The default global hotkey is **Scroll Lock** (In german: "rollen").
You can change it via the `--hotkey` option (see below).
Proposal for alternative key: `ctrl_r`, `alt_r`, `cmd_r`, `shift_r` ;)

## CLI listen

[comment]: <> (✂✂✂ auto generated listen help start ✂✂✂)
```
usage: stt2desktop listen [-h] [LISTEN OPTIONS]

Start the STT listener. Hold the hotkey to record, release to transcribe and insert.

╭─ options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help                show this help message and exit                                                            │
│ -v, --verbosity           Verbosity level; e.g.: -v, -vv, -vvv, etc. (repeatable)                                    │
│ --model {tiny_en,tiny,base_en,base,small_en,small,medium_en,medium,large_v1,large_v2,large_v3,large,distil_large_v2, │
│ distil_medium_en,distil_small_en,distil_large_v3,distil_large_v3_5,large_v3_turbo,turbo}                             │
│                           Whisper model to use for transcription. (default: small)                                   │
│ --hotkey {alt,alt_l,alt_r,alt_gr,backspace,caps_lock,cmd,cmd_l,cmd_r,ctrl,ctrl_l,ctrl_r,delete,down,end,enter,esc,   │
│ f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,home,left,page_down,page_up,right,shift,      │
│ shift_l,shift_r,space,tab,up,media_play_pause,media_volume_mute,media_volume_down,media_volume_up,media_previous,    │
│ media_next,insert,menu,num_lock,pause,print_screen,scroll_lock}                                                      │
│                           Key to hold for recording. Release to transcribe and insert text. Proposal for alternative │
│                           key: ctrl_r, alt_r, cmd_r, shift_r. (default: scroll_lock)                                 │
│ --sample-rate INT         Audio sample rate in Hz. Whisper expects 16000. (default: 16000)                           │
│ --device STR              Device to run inference on, e.g. cpu or cuda. (default: auto)                              │
│ --compute-type STR        Quantization type, e.g. int8, float16, float32. (default: int8)                            │
│ --num-workers {None}|INT  Number of parallel transcription workers. Defaults to CPU count. (default: None)           │
│ --sounds, --no-sounds     Play notification sounds via chime. (default: True)                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated listen help end ✂✂✂)


### Whisper models

Just a selection and approximate values:

| Model    | Size    | Speed   | Accuracy         |
|----------|---------|---------|------------------|
| `tiny`   | ~75 MB  | fastest | lowest           |
| `base`   | ~145 MB | fast    | good             |
| `small`  | ~460 MB | slower  | better (default) |
| `medium` | ~1.5 GB | slow    | high             |

Larger models produce more accurate transcriptions but take longer to process ;)


## start development

At least `uv` is needed. Install e.g.: via pipx:
```bash
apt-get install pipx
pipx install uv
```

Clone the project and just start the CLI help commands.
A virtual environment will be created/updated automatically.

```bash
~$ git clone https://github.com/jedie/stt2desktop.git
~$ cd stt2desktop
~/stt2desktop$ ./cli.py --help
~/stt2desktop$ ./dev-cli.py --help
```

[comment]: <> (✂✂✂ auto generated dev help start ✂✂✂)
```
usage: ./dev-cli.py [-h] {coverage,install,lint,mypy,nox,pip-audit,publish,test,update,update-readme-history,update-test-snapshot-files,version}



╭─ options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help    show this help message and exit                                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ subcommands ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ (required)                                                                                                           │
│   • coverage  Run tests and show coverage report.                                                                    │
│   • install   Install requirements and 'stt2desktop' via pip as editable.                                            │
│   • lint      Check/fix code style by run: "ruff check --fix"                                                        │
│   • mypy      Run Mypy (configured in pyproject.toml)                                                                │
│   • nox       Run nox                                                                                                │
│   • pip-audit                                                                                                        │
│               Run pip-audit check against current requirements files                                                 │
│   • publish   Build and upload this project to PyPi                                                                  │
│   • test      Run unittests                                                                                          │
│   • update    Update dependencies (uv.lock) and git pre-commit hooks                                                 │
│   • update-readme-history                                                                                            │
│               Update project history base on git commits/tags in README.md Will be exited with 1 if the README.md    │
│               was updated otherwise with 0.                                                                          │
│                                                                                                                      │
│               Also, callable via e.g.:                                                                               │
│                   python -m cli_base update-readme-history -v                                                        │
│   • update-test-snapshot-files                                                                                       │
│               Update all test snapshot files (by remove and recreate all snapshot files)                             │
│   • version   Print version and exit                                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated dev help end ✂✂✂)


## History

[comment]: <> (✂✂✂ auto generated history start ✂✂✂)

* [**dev**](https://github.com/jedie/stt2desktop/compare/v0.1.1...main)
  * 2026-03-27 - Update README
* [v0.1.1](https://github.com/jedie/stt2desktop/compare/v0.1.0...v0.1.1)
  * 2026-03-27 - +Proposal for alternative hotkey
  * 2026-03-27 - fix color outputs
  * 2026-03-27 - Update requirements
  * 2026-03-27 - add missing license file.
* [v0.1.0](https://github.com/jedie/stt2desktop/compare/v0.0.1...v0.1.0)
  * 2026-03-27 - Use chime to play notification sounds
  * 2026-03-27 - Try to fix github CI run
  * 2026-03-27 - Cleanup README
  * 2026-03-27 - pipx usage
* [v0.0.1](https://github.com/jedie/stt2desktop/compare/b407f8f...v0.0.1)
  * 2026-03-26 - Add POC
  * 2026-03-26 - init

[comment]: <> (✂✂✂ auto generated history end ✂✂✂)
