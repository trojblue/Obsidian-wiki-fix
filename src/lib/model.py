SOURCE_DIR = "D:\quartz\content-edit"
OUTPUT_DIR = "D:\quartz\content"
INDEX_JSON_PATH = "D:\quartz\\assets\indices\contentIndex.json"

# SOURCE_DIR = "D:\CSC2\Obsidian-wiki-fix\\test_lib"
# OUTPUT_DIR = "D:\CSC2\Obsidian-wiki-fix\\test_out"

MARKDOWN_EXTENSIONS = [".md", ".markdown"]

# https://help.obsidian.md/Advanced+topics/Accepted+file+formats
# listing ALL of them because github recognizes upper/lowercase as different
IMAGE_EXTENSIONS = [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg",
                    ".JPEG", ".JPG", ".PNG", ".GIF", ".BMP", ".SVG"]


# useless
re_md_start_old = "```[^\S\r\n]*[a-zA-Z0-9_\-\(\)]*[\r\n]$"

# starts with ```, any other characters, should not end with ```
re_md_start = "^```[\w\-\(\)^\S]*[^`]*$"

# ``` with text after it is still considered to be in block
re_md_end = "```$"

# referenced wiki-link have ! in front
re_md_reference = ".*\!\[\[(?!.+?:)([^\]\[]+)\]\]"

# CHECK PARTIAL FIRST before heading to second one
# eg. [[it_has_partial#partial]]
re_md_wiki_partial = ".*\[\[(?!.+?:)([^\]\[]+)#([^\]\[]+)\]\]"

# this will return true if string has # as well
re_md_wiki = ".*\[\[(?!.+?:)([^\]\[]+)\]\]"
