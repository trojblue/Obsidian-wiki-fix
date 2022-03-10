import glob
import os
import re
import shutil
from typing import *

from lib.controller import *
from lib.model import *


def is_code_start(line: str) -> bool:
    """
    check if the line is a md codeblock start
    :param line: eg. "```pythonic\n"
    """
    start_rule = re.compile(re_md_start)
    match = re.search(start_rule, line)
    return bool(match)


def is_code_end(line: str) -> bool:
    """
    check if the line is a md codeblock end
    :param line: eg. "```"
    """
    end_rule = re.compile(re_md_end)
    match = re.search(end_rule, line)
    return bool(match)


def get_extension(path: str) -> Tuple:
    """return filename, file_extension"""
    return os.path.splitext(path)


def get_root_path(dir_name):
    # lazy way to get root
    for path, currentDirectory, files in os.walk(top=dir_name):
        root_path = path
        return root_path


def get_relative_path(full_path: str, root_path: str):
    """
    :param full_dir: "D:\CSC2\obsidian_abs\working_lib\_index.md"
    :param root_dir: "D:\CSC2\obsidian_abs\working_lib"
    :return: _index.md
    """
    if root_path in full_path:
        subtracted = full_path.replace(root_path + '\\', '')
        return subtracted.replace(os.sep, '/')  # change to linux slash
    else:
        print("ERROR: inconsistent dir")


def read_file(path: str) -> List[str]:
    """
    read in a md file
    :param path: relative path (of INPUT_DIR) to be saved
    :return: List of lines
    """
    full_read_path = os.path.join(SOURCE_DIR, path)
    a_file = open(full_read_path, "r")
    lines = a_file.readlines()
    a_file.close()
    return lines


def copy_overwrite_source():
    """
    copy every file from SOURCE_DIR to OUTPUT_DIR
    needs Python 3.8 new feature
    :return: None
    """
    files = glob.glob(OUTPUT_DIR)
    for f in files:
        os.remove(f)

    shutil.copytree(SOURCE_DIR, OUTPUT_DIR, dirs_exist_ok=True)


def save_file(str_list: List[str], path: str):
    """
    :param file: list of lines
    :param path: relative path (of OUTPUT_DIR) to be saved
    :return:
    """
    full_save_path = os.path.join(OUTPUT_DIR, path)
    f = open(full_save_path, "w")
    for element in str_list:
        f.write(element + "\n")
    f.close()


def change_json_slash():
    json_lines = read_file(INDEX_JSON_PATH)
    for i in range (len(json_lines)):
        curr_line = json_lines[i]
        json_lines[i] = curr_line.replace("\\\\", "/")

        print("D")
