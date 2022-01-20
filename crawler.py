
import os
import json
import heapq
import markdown
from collections import defaultdict
import frontmatter

PAGES_DIR = "./blobs"


def parse_path(path):
    if "/" in path:
        dir_name, file_name = path.split("/")
    else:
        dir_name, file_name = "", path
    return dir_name, file_name


def parse_filename(name):
    if name.endswith(".md"):
        return name[:-3]


class Crawler():
    def __init__(self):
        self.root = defaultdict(lambda: {})
        self.sidebar = defaultdict(lambda: [])

    async def setup(self):
        await self.build()
        # rearrange sidebar according to priority using a priority queue
        for folder in self.sidebar:
            heapq.heapify(self.sidebar[folder])

    def read_page(self, dir, file_name):
        path = f"{PAGES_DIR}/{dir}/{file_name}"
        if os.path.exists(path):
            post = frontmatter.load(path)
            res = {"content": post.content}
            for key in post.keys():
                res[key] = post[key]
            return res
        else:
            return None

    def get_logo(self):
        f = open("logo.svg", "r")
        res = f.read()
        f.close()
        return res

    async def build(self, dir=""):
        with os.scandir(f"{PAGES_DIR}/{dir}") as entries:
            for entry in entries:
                if entry.is_dir():
                    await self.build(entry.name)
                else:

                    if not entry.name.endswith(".md"):
                        continue

                    res = self.read_page(dir, entry.name)

                    if not res:
                        continue

                    self.sidebar[str(res["parent"])].append(
                        (int(res["position"]), {"name": str(res["name"]), "filename": parse_filename(entry.name)}))
                    self.root[str(res["parent"])
                              ][parse_filename(entry.name)] = res

    def page_content(self, path):
        dir_name, file_name = parse_path(path)

        if not self.root.get(dir_name) or not self.root.get(dir_name).get(file_name):
            return None
        raw_content = self.root.get(dir_name).get(file_name)["content"]
        return markdown.markdown(raw_content)

    def get_template_data(self, path=None):
        if not path:
            # on / route renders the first page
            dir_name = list(self.sidebar.keys())[0]
            file_name = self.sidebar[dir_name][0][1]["filename"]
        else:
            dir_name, file_name = parse_path(path)
        if not self.root.get(dir_name) or not self.root.get(dir_name).get(file_name):
            return None
        blob = self.root.get(dir_name).get(file_name)
        res = {
            "title": "Peaks",
            "key": file_name,
            "sidebar": self.sidebar,
            "note": markdown.markdown(blob["content"]),
            "path": path,
            "svg": self.get_logo()
        }

        return res
