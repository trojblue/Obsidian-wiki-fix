from lib.handlers import *
from lib.helpers import *
from typing import *
import re

# todo: add other extensions



def get_md_list(folder_dict: Dict) -> List:
    """return a list of md file routes relative to SOURCE_DIR
    eg. ['test.md', 'folder/wiki.md', ]
    """
    md_list = []
    for i in folder_dict.keys():
        if not get_extension(i)[1]:  # markdown files have no suffix in name
            md_list.append(folder_dict[i])

    return md_list


def replace_if_has_wiki_link(line: str, folder_dict: Dict) -> Tuple[str, int]:
    """  ^title
    :return: (string with all wikis replaced, replacement count)
    """
    embed_rule = re.compile(re_md_reference)
    wiki_partial_rule = re.compile(re_md_wiki_partial)
    wiki_rule = re.compile(re_md_wiki)
    new_line = line
    wiki_count = 0

    # ![[xxxx.png]] -> ![xxx](...xxxx.png)
    while (match := re.search(embed_rule, new_line)):
        new_line = handle_rewrite(match, new_line, folder_dict, "embed")
        wiki_count += 1

    # [[xxxx|yyy]] -> [[yyy]](...xxxx.md)  todo: not implemented
    while (match := re.search(wiki_partial_rule, new_line)):
        new_line = handle_rewrite(match, new_line, folder_dict, "md_partial")
        wiki_count += 1

    # [[xxxx]] -> [xxx](...xxxx.md)
    while (match := re.search(wiki_rule, new_line)):
        new_line = handle_rewrite(match, new_line, folder_dict, "md")
        wiki_count +=1

    # new_line=line if no changes made
    return new_line, wiki_count


def convert_lines(lines: List, folder_dict: Dict) -> Tuple[List, int]:
    """
    :param lines: List of lines
    :return: List[lines with wiki-link] to convert, converted lines count
    https://stackoverflow.com/questions/64111377/remove-markdown-code-block-from-python-string
    """
    is_in_code_block = False
    found_count = 0

    for i in range(len(lines)):

        # skipping parts that are wrapped in ``` code blocks ```
        if is_code_start(lines[i]) and not is_in_code_block:
            is_in_code_block = True

        elif is_code_end(lines[i]):
            is_in_code_block = False

        elif (is_in_code_block):
            continue

        else:  # not in code block; todo: modify lines
            lines[i], curr_found_count = replace_if_has_wiki_link(lines[i], folder_dict)
            found_count += curr_found_count

    return lines, found_count


if __name__ == '__main__':
    print("===This is the controller, and you shouldn't really be running this!===")
