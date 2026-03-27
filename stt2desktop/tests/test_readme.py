from bx_py_utils.auto_doc import assert_readme_block
from bx_py_utils.path import assert_is_file
from cli_base.cli_tools.test_utils.assertion import assert_in
from cli_base.cli_tools.test_utils.rich_test_utils import NoColorEnvRich, invoke
from manageprojects.tests.base import BaseTestCase

from stt2desktop import constants
from stt2desktop.cli_dev import PACKAGE_ROOT
from stt2desktop.constants import DEFAULT_WHISPER_NUM_WORKERS


def assert_cli_help_in_readme(text_block: str, marker: str):
    README_PATH = PACKAGE_ROOT / 'README.md'
    assert_is_file(README_PATH)

    text_block = text_block.replace(constants.CLI_EPILOG, '')
    text_block = f'```\n{text_block.strip()}\n```'
    assert_readme_block(
        readme_path=README_PATH,
        text_block=text_block,
        start_marker_line=f'[comment]: <> (✂✂✂ auto generated {marker} start ✂✂✂)',
        end_marker_line=f'[comment]: <> (✂✂✂ auto generated {marker} end ✂✂✂)',
    )


class ReadmeTestCase(BaseTestCase):
    # Note: Activate main --help only, after we add more commands ;)
    # def test_main_help(self):
    #     with NoColorEnvRich():
    #         stdout = invoke(
    #             cli_bin=PACKAGE_ROOT / 'cli.py',
    #             args=['--help'],
    #             strip_line_prefix='usage: ',
    #         )
    #     assert_in(
    #         content=stdout,
    #         parts=(
    #             'usage: stt2desktop [-h]',
    #             ' version ',
    #             'Print version and exit',
    #             constants.CLI_EPILOG,
    #         ),
    #     )
    #     assert_cli_help_in_readme(text_block=stdout, marker='main help')

    def test_listen_help(self):
        with NoColorEnvRich():
            stdout = invoke(
                cli_bin=PACKAGE_ROOT / 'cli.py',
                args=['listen', '--help'],
                strip_line_prefix='usage: stt2desktop listen ',
            )
        cpu_count_part = f'Defaults to CPU count. (default: {DEFAULT_WHISPER_NUM_WORKERS})'
        assert_in(
            content=stdout,
            parts=(
                'usage: stt2desktop listen ',
                ' --hotkey ',
                ' --model ',
                cpu_count_part,
            ),
        )
        stdout = stdout.replace(cpu_count_part, 'Defaults to CPU count. (default:XY)').strip()
        assert_cli_help_in_readme(text_block=stdout, marker='listen help')

    def test_dev_help(self):
        with NoColorEnvRich():
            stdout = invoke(
                cli_bin=PACKAGE_ROOT / 'dev-cli.py',
                args=['--help'],
                strip_line_prefix='usage: ',
            )
        assert_in(
            content=stdout,
            parts=(
                'usage: ./dev-cli.py [-h]',
                ' lint ',
                ' coverage ',
                ' update-readme-history ',
                ' publish ',
                constants.CLI_EPILOG,
            ),
        )
        assert_cli_help_in_readme(text_block=stdout, marker='dev help')
