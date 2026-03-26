import functools
import shutil
import sys
from pathlib import Path

from cli_base.cli_tools.subprocess_utils import verbose_check_call


def get_bin(name: str, hint: str) -> Path:
    bin_path = shutil.which(name)
    if bin_path is None:
        print(f'[red]Error: {name} is not installed or not found in PATH.[/red]')
        print(hint)
        sys.exit(1)
    return Path(bin_path)


@functools.cache
def get_wtype_bin() -> Path:
    wtype_bin = get_bin('wtype', hint='wtype is required for Wayland support: sudo apt install wtype')
    verbose_check_call(wtype_bin, 'version')
    return wtype_bin


@functools.cache
def get_xdotool_bin() -> Path:
    xdotool_bin = get_bin('xdotool', hint='xdotool is required for X11 support: sudo apt install xdotool')
    verbose_check_call(xdotool_bin, 'version')
    return xdotool_bin
