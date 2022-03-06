# Obsidian-wiki-fix
The project is intended to convert Obsidian wiki-link to Quartz-supported markdown relative links, plus the benefit of easily customizing output scheme to fit any other software/service.

**Requires python version > 3.8** because I used `:=` and some other python38 features.

Decently documented so it's easier to modify by your needs.

suffixes such as `PNG` and `png` are treated as different files to better support github pages functionality. 




## Usage

1. clone repo
2. change `SOURCE_DIR` to your obsidian vault folder
3. change `OUTPUT_DIR` to folders of your choice
4. run `src/view.py`

The converted obsidian vault will be copied to your specified `OUTPUT_DIR`.




## Sample Results

```
Original:
![[Pasted image 20220305175334.PNG]]

    Converts to:
    ![Pasted image 20220305175334.PNG](==assets==/Pasted image 20220305175334.PNG)


Original:
[[nested_child]]

    Converts to:
    [nested_child](English_folder/nested_child.md)
```



## Known Issues

these types of links are not working for now:

```
[[something#chapter]]
[[something|displayedTitle]]
[[something#chapter|displayedTitle]]
```

also audio / pdf and stuff are not supported. only text and image, but they're easy to implement. Just the fact that I don't use them very often.





## Disclaimer

Tested working on windows; might need minor modifications on other OS because of how path works differently.

Please note that it's just a personal script to get the jobs done. The code is open source and feel free to review it.

 **In the highly unlikely case that the script damaged your vault, I hold no accountability for any financial loss.** I understand that personal knowledge bases are invaluable, so please do take backups regularly. I wouldn't recommend using the converted base as a main. Use the script only to publish online, so you won't lose the original vault in case I wrote anything wrong.

Also do let me know if you find any issues!
