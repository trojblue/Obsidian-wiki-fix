import re
from typing import *
from helpers import *


def get_new_line(match: re.Match, line: str, folder_dict: Dict, mode: str):
    """
    :param line: one line in file
    :param mode: "embed, md, md_hash"
    :return: modified line
    """
    curr_interval = match.span(1)  # (start, end)
    full_name = f'{match.group(1)}'
    filename, file_extension = get_extension(full_name)

    # TODO: pretty print; point to default img if not found
    relative_dir = folder_dict[full_name] if full_name in folder_dict.keys() else ""
    print(full_name, "  ->  ", relative_dir)

    if mode == "embed":
        if not file_extension:
            return handle_md_embed(full_name, line, relative_dir, curr_interval)
        else:
            return handle_image(full_name, line, relative_dir, curr_interval)

    elif mode == "md_partial":
        return handle_md_partial(full_name, line, relative_dir, curr_interval)

    elif mode == "md":
        return handle_md(full_name, line, relative_dir, curr_interval)


def handle_image(filename, line, relative_dir, curr_interval) -> str:
    """
    :param filename: ***.png
    :param line:  one line in file
    :param curr_interval: (start, end)
    :return: modified line
    """
    start, end = curr_interval  # start, end: to include [[ ]]  at front & back
    start -= 3
    end += 2
    md_relative_path = '![' + filename + '](' + relative_dir + ')'
    new_line = line[0:start] + md_relative_path + line[end:]
    return new_line


def handle_md_embed(filename, line, relative_dir, curr_interval) -> str:
    """
    convert embedded markdown to normal reference
    """
    start, end = curr_interval
    start -= 3
    end += 2
    md_relative_path = '[' + filename + '](' + relative_dir + ')'
    new_line = line[0:start] + md_relative_path + line[end:]
    return new_line


def handle_md(filename, line, relative_dir, curr_interval) -> str:
    """
    :param filename: ***  (no .md)
    """
    start, end = curr_interval
    start -= 2
    end += 2
    md_relative_path = '[' + filename + '](' + relative_dir + ')'
    new_line = line[0:start] + md_relative_path + line[end:]
    return new_line


def handle_md_partial(filename, line, relative_dir, curr_interval) -> str:
    # TODO: not implemented

    start, end = curr_interval
    start -= 2
    end += 2
    md_relative_path = '[' + filename + '](' + relative_dir + ')'
    new_line = line[0:start] + md_relative_path + line[end:]
    return new_line
