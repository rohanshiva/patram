## More about file and folder names
> If you have multiple folder's with the same name but different position, then one of them is discarded. 

E.g.
If you have a structure like this:
```bash
pages
    - 1-folder-one
        - 1-intro.md
    - 2-folder-one
        - 1-getting-started.md
```

Only `1-folder-one` is parsed by the app.

> If you have multiple files with the same name and same parent but different position, then only one of them is parsed.

E.g.
```bash
pages
    - 1-getting-started
        -  1-intro.md
        -  2-intro.md
```

Only the content of `2-intro.md` is parsed by the app. However, same file names with different parents work as expected.

## Reserved Names
Please try to avoid using `images` and `favicons` as parent folder names, as those routes are reserved by the app to retrieve images and favicons respectively. However, if you really need to use those names modify the app router accordingly (main.py). 