# Obsidian-wiki-fix

Converts Obsidian wiki-link to markdown relative links for [Quartz](https://github.com/jackyzha0/quartz), plus the benefit of easily customizing output scheme to fit any other software/service.

**Requires python version > 3.8** because I used `:=` and some other python38 features.

Decently documented so it's easier to modify by your needs.

## Usage

**The script is intended for "shortest possible" (`[[something]]`)style of wiki-link in obsidian settings.**

**convert only:**

```bash
git clone https://github.com/trojblue/Obsidian-wiki-fix && cd Obsidian-wiki-fix/src
```

1. edit `/src/model.py`:
   1. change `SOURCE_DIR` to your obsidian vault folder
   2. change `OUTPUT_DIR` to folder of your choice
2. run `src/app.py`, the converted obsidian vault will be copied to your specified `OUTPUT_DIR`.

**convert and push:**

1. finish step 1 as above
2. edit & run `update.bat` according to your local path

You can also automate things like generating YAML before publishing, or add backlink/tags to similar articles. Python would come in handy when doing NLP stuff.

## Sample Results

see `sample_lib` folder for the actual hierarchy.

suffixes such as `PNG` and `png` are treated as different files to better support github pages functionality.

```
![[Pasted image 20220305175334.PNG]]
    →
    ![Pasted image 20220305175334.PNG](==assets==/Pasted image 20220305175334.PNG)

[[nested_child]]
    →
    [nested_child](English_folder/nested_child.md)
```

## Known Issues

**filename with space is not supported for now, to be fixed**

these types of links are not working for now:

```
[[something#chapter]]
[[something|displayedTitle]]
[[something#chapter|displayedTitle]]
```

also audio / pdf and stuff are not supported. only text and image, but others are easy to implement. Just the fact that I don't use them very often.

## Disclaimer

Tested working on windows; might need minor modifications on other OS because of how path works differently.

Please note that it's just a personal script to get the jobs done. The code is open source and feel free to review it.

**In the highly unlikely case that the script damaged your vault, I hold no accountability for any financial loss.** I understand that personal knowledge bases are invaluable, so please do take backups regularly. I wouldn't recommend using the converted base as a main. Use the script only to publish online, so you won't lose the original vault in case I wrote anything wrong.

Also do let me know if you find any issues!
