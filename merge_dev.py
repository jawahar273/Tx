import os
from typing import Sequence
import click

from colorama import init
from termcolor import colored

init()

import pytest

ROOT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PRODUCTION_DIR_PATH = None
PRODUCTION_FILE_PATHS = None
_FILE_PATH = None


def get_env_files():
    """
    Set the file path for the .env file for merging
    between different dot files inside the given
    folder.
    """
    global PRODUCTION_DIR_PATH
    global PRODUCTION_FILE_PATHS
    global _FILE_PATH

    PRODUCTION_DIR_PATH = os.path.join(ROOT_DIR_PATH, ".envs", ".local")

    PRODUCTION_FILE_PATHS = [
        os.path.join(PRODUCTION_DIR_PATH, ".general"),
        os.path.join(PRODUCTION_DIR_PATH, ".sanic"),
        os.path.join(PRODUCTION_DIR_PATH, ".postgres"),
        # os.path.join(PRODUCTION_DIR_PATH, ".password"),
        os.path.join(PRODUCTION_DIR_PATH, ".txbot"),
    ]
    # env_root_path = [".envs", ".local"]
    _FILE_PATH = os.path.join(ROOT_DIR_PATH, ".env")


def get_git_ignore():
    """
    Set the file path for the .gitignore file for merging
    between different dot files inside the given
    folder.
    """
    global PRODUCTION_DIR_PATH
    global PRODUCTION_FILE_PATHS
    global _FILE_PATH

    PRODUCTION_DIR_PATH = os.path.join(ROOT_DIR_PATH, ".gitignores")
    PRODUCTION_FILE_PATHS = [
        # os.path.join(PRODUCTION_DIR_PATH, ".general"),
        os.path.join(PRODUCTION_DIR_PATH, ".python"),
        # os.path.join(PRODUCTION_DIR_PATH, ".client"),
    ]
    # path of the folders.

    _FILE_PATH = os.path.join(ROOT_DIR_PATH, ".gitignore")


def merge(
    output_file_path: str, merged_file_paths: Sequence[str], append_linesep: bool=True
) -> None:
    with open(output_file_path, "w") as output_file:
        for merged_file_path in merged_file_paths:
            with open(merged_file_path, "r") as merged_file:
                merged_file_content = merged_file.read()
                output_file.write(merged_file_content)
                if append_linesep:
                    output_file.write(os.linesep)


@click.command()
@click.option("--env", "-e", help="env files", default=False)
@click.option("--git", "-g", help="gitignore file", default=False)
def main(env, git):

    if env:

        click.echo(
            colored(
                "Please set .password file inside\
                the .envs folder for dev..",
                "yellow",
            )
        )
        get_env_files()

    elif git:

        get_git_ignore()
    else:
        click.echo("Neither option is selected")
        return
    merge(_FILE_PATH, PRODUCTION_FILE_PATHS)


@pytest.mark.parametrize("merged_file_count", range(3))
@pytest.mark.parametrize("append_linesep", [True, False])
def test_merge(tmpdir_factory, merged_file_count: int, append_linesep: bool):
    tmp_dir_path = str(tmpdir_factory.getbasetemp())

    output_file_path = os.path.join(tmp_dir_path, ".env")

    expected_output_file_content = ""
    merged_file_paths = []
    for i in range(merged_file_count):
        merged_file_ord = i + 1

        merged_filename = ".service{}".format(merged_file_ord)
        merged_file_path = os.path.join(tmp_dir_path, merged_filename)

        merged_file_content = merged_filename * merged_file_ord

        with open(merged_file_path, "w+") as file:
            file.write(merged_file_content)

        expected_output_file_content += merged_file_content
        if append_linesep:
            expected_output_file_content += os.linesep

        merged_file_paths.append(merged_file_path)

    merge(output_file_path, merged_file_paths, append_linesep)

    with open(output_file_path, "r") as output_file:
        actual_output_file_content = output_file.read()

    assert actual_output_file_content == expected_output_file_content


if __name__ == "__main__":
    main()
