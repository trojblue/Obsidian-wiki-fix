from model import *
from routes import *
from helpers import *


# todo: add other extensions


def get_md_list(folder_dict:Dict)->List:
    """return a list of md file routes relative to SOURCE_DIR
    eg. ['test.md', 'folder/wiki.md', ]
    """
    md_list = []
    for i in folder_dict.keys():
        nm = get_extension(i)[1]
        if not get_extension(i)[1]: # markdown files have no suffix in name
            md_list.append(folder_dict[i])

    return md_list


def replace_if_has_double_quote(line:str, folder_dict:Dict) -> str:
    embed_rule = re.compile(re_md_reference)
    wiki_partial_rule = re.compile(re_md_wiki_partial)
    wiki_rule = re.compile(re_md_wiki)


    new_line = line

    # ![[xxxx.png]] -> ![xxx](...xxxx.png)
    # todo: add markdown rewrite
    while(recursive_match := re.search(embed_rule, new_line)):
        new_line = get_new_line(recursive_match, new_line, folder_dict, "embed")

    while(recursive_match := re.search(wiki_partial_rule, new_line)):
        new_line = get_new_line(recursive_match, new_line, folder_dict, "md_partial")

    # [[xxxx]] -> [xxx](...xxxx.md)
    while(recursive_match := re.search(wiki_rule, new_line)):
        new_line = get_new_line(recursive_match, new_line, folder_dict, "md")

    # [[xxx]] not found
    return new_line


def convert_lines(lines:List, folder_dict:Dict) -> List:
    """
    :param lines: List of lines
    :return: List[lines with wiki-link] to convert
    https://stackoverflow.com/questions/64111377/remove-markdown-code-block-from-python-string
    """
    is_in_code_block = False

    for i in range(len(lines)):
        if is_code_start(lines[i]) and not is_in_code_block:
            is_in_code_block = True

        elif is_code_end(lines[i]):
            is_in_code_block = False

        elif (is_in_code_block):
            continue

        else: # normal text not in code block
            # todo: modify lines
            new_line = replace_if_has_double_quote(lines[i], folder_dict)
            lines[i] = new_line
            continue

    return lines



if __name__ == '__main__':
    # a = replace_if_has_double_quote("这是一段[[asd中文as日本語#asd]]")
    # b = is_code_start("```  asdas dasd```")
    print("D")
