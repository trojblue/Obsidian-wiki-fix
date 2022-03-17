from lib.controller import *
from lib.helpers import *


def parse_folder_to_dicts(dir_name: SOURCE_DIR) -> Tuple[dict, List]:
    """
    :param dir_name: folder absolute dir
    :return: 2 Dicts:  { file_name: linux path}, [os path for markdown files]
    """
    out_dict = {}
    md_list = []
    root_path = get_root_path(dir_name)

    for path, currentDirectory, files in os.walk(top=dir_name):
        for file in files:  # '_index.md' in ['', '', '' ]
            get_file_info(file, md_list, out_dict, path, root_path)

    return out_dict, md_list


def get_file_info(file, md_list, out_dict, path, root_path):
    """
    update md_list and out_dict info of a single file
    """

    # '../working_lib/_index.md'
    full_path = os.path.join(path, file)
    # `_index`    `.md`
    filename, file_extension = get_extension(file)

    if (file_extension in CONVERT_EXTENSIONS):  # is markdown
        if (filename) in out_dict:
            # file with same name exists
            print("ERROR: markdown file %s already exists" % file)
        else:
            relative_path = get_relative_path(full_path, root_path)
            out_dict[filename] = relative_path
            md_list.append(relative_path)

    elif (file_extension in IMAGE_EXTENSIONS):  # is image
        if (file) in out_dict:
            # file with same name exists
            print("ERROR: image file %s already exists" % file)
        else:
            out_dict[file] = get_relative_path(full_path, root_path)



def handle_wiki():
    """Main Program for rewriting wiki links
    """
    # { file_name: linux path}, [os path for markdown files]
    print("rewriting wiki-links...")
    folder_dict, md_list = parse_folder_to_dicts(SOURCE_DIR)
    wiki_foler_count = 0

    for path in md_list:
        curr_lines = read_file(path)
        new_lines, wiki_file_count = convert_lines(curr_lines, folder_dict)
        save_file(new_lines, path)
        wiki_foler_count += wiki_file_count

    print("replaced %s links in %s files"%(wiki_foler_count, len(folder_dict.keys())) )

def run():
    copy_overwrite_source()
    handle_wiki()
    # change_json_slash()

if __name__ == '__main__':
    run()