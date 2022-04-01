# Patram
##### /pa-thrum/ (Leaf 🍃 in Sanskrit) 

Patram is a documentation site builder that is simple, easy to use, 🔥 customizable, and ✨ looking! Simply write your `.md` files and deploy your site with  **one** command**!** 

## Features
- Docs are server side rendered -> **SEO** 🚀 
- No build step! 🏭 ❌
- Built for customization 🎨
- Simple & small codebase 🤏
- Dark mode 👾
- Deploy with one command 🤘🏿

## Basic Usage
### Installation
To get started, clone this [🔗 this repo](https://github.com/rohanshiva/patram) to your desired location on your machine.
```bash
https://github.com/rohanshiva/patram.git
```
This will get you a copy of patram. Follow the next few steps to fully customize it and make it yours!
Now, type `pip install -r requirements.txt` to install all the necessary dependencies.

### Adding pages
Navigate to the root dir of the project.
```bash
cd patram
```

> patram currently supports only one parent dir.
Simply add `.md` files to `pages/` with the proper format. 

All files under `pages/` are in the root dir (no parent). If you want to add files under one level or parent, add your `.md` pages to a folder inside `/pages/`.

#### Naming Standard
All file and folder names should follow the following naming standard.
- lowercase
- replace ' ' (spaces) with '-'
- words should be seperated by -
- try to avoid special characters
- names should trail with a number to indicate position 

In general pages under root dir follow `/pages/{position-page-name.md}`. Pages under a parent dir follow `/pages/{position-folder-name.md}/{position-page-name.md}`

**E.g.** 
```bash
pages
    - 1-readme.md
    - 1-getting-started
        - 1-introduction.md
        - 2-installation.md
    - 2-examples
        - 1-one.md
        - 2-two.md
        - 3-three.md
```
Sidebar : 

![Example structure](/images/example_structure.png)

To deploy your app, follow [this guide](/getting-started/deploy-your-app).

### Running locally
To run the app locally, simply run the following commands from the root project dir.

```bash
uvicorn main:app --reload
```

Your app should be live at [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)! 🎆


