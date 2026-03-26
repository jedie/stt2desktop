# stt2kde

[![tests](https://github.com/jedie/stt2kde/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/jedie/stt2kde/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/stt2kde/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/stt2kde)
[![stt2kde @ PyPi](https://img.shields.io/pypi/v/stt2kde?label=stt2kde%20%40%20PyPi)](https://pypi.org/project/stt2kde/)
[![Python Versions](https://img.shields.io/pypi/pyversions/stt2kde)](https://github.com/jedie/stt2kde/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/stt2kde)](https://github.com/jedie/stt2kde/blob/main/LICENSE)

local STT for KDE using faster-whisper

## CLI

[comment]: <> (✂✂✂ auto generated main help start ✂✂✂)
```
usage: ./cli.py [-h] {shell-completion,version}



╭─ options ─────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help            show this help message and exit                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
╭─ subcommands ─────────────────────────────────────────────────────────────────────────────╮
│ (required)                                                                                │
│   • shell-completion  Setup shell completion for this CLI (Currently only for bash shell) │
│   • version           Print version and exit                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated main help end ✂✂✂)


## start development

At least `uv` is needed. Install e.g.: via pipx:
```bash
apt-get install pipx
pipx install uv
```

Clone the project and just start the CLI help commands.
A virtual environment will be created/updated automatically.

```bash
~$ git clone https://github.com/jedie/stt2kde.git
~$ cd stt2kde
~/stt2kde$ ./cli.py --help
~/stt2kde$ ./dev-cli.py --help
```

[comment]: <> (✂✂✂ auto generated dev help start ✂✂✂)
```
usage: ./dev-cli.py [-h] {coverage,install,lint,mypy,nox,pip-audit,publish,shell-completion,test,update,update-readme-history,update-test-snapshot-files,version}



╭─ options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help     show this help message and exit                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ subcommands ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ (required)                                                                                                           │
│   • coverage   Run tests and show coverage report.                                                                   │
│   • install    Install requirements and 'stt2kde' via pip as editable.                                     │
│   • lint       Check/fix code style by run: "ruff check --fix"                                                       │
│   • mypy       Run Mypy (configured in pyproject.toml)                                                               │
│   • nox        Run nox                                                                                               │
│   • pip-audit  Run pip-audit check against current requirements files                                                │
│   • publish    Build and upload this project to PyPi                                                                 │
│   • shell-completion                                                                                                 │
│                Setup shell completion for this CLI (Currently only for bash shell)                                   │
│   • test       Run unittests                                                                                         │
│   • update     Update dependencies (uv.lock) and git pre-commit hooks                                                │
│   • update-readme-history                                                                                            │
│                Update project history base on git commits/tags in README.md Will be exited with 1 if the README.md   │
│                was updated otherwise with 0.                                                                         │
│                                                                                                                      │
│                Also, callable via e.g.:                                                                              │
│                    python -m cli_base update-readme-history -v                                                       │
│   • update-test-snapshot-files                                                                                       │
│                Update all test snapshot files (by remove and recreate all snapshot files)                            │
│   • version    Print version and exit                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated dev help end ✂✂✂)


## History

[comment]: <> (✂✂✂ auto generated history start ✂✂✂)



[comment]: <> (✂✂✂ auto generated history end ✂✂✂)
