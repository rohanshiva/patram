import os
from highlight_renderer import markdown
import frontmatter
import urllib
from config import get_parent_position

PAGES_DIR = "./pages"


def get_filename(entry_name):
    return entry_name[:-3]


class Crawler:
    def __init__(self):
        self.sidebar = {}

    async def setup(self):
        await self.build()
        # rearrange sidebar according to priority
        await self.sort_sidebar()
        print(self.sidebar)

    async def sort_sidebar(self):
        self.sidebar = dict(
            sorted(self.sidebar.items(), key=lambda dir: dir[1]["position"])
        )
        for dir in self.sidebar:
            self.sidebar[dir]["children"] = dict(
                sorted(
                    self.sidebar[dir]["children"].items(),
                    key=lambda file: file[1]["position"],
                )
            )

    def read_page_content(self, path):
        path = f"{PAGES_DIR}/{path}.md"
        if os.path.exists(path):
            post = frontmatter.load(path)
            return markdown(post.content)
        else:
            return None

    async def read_page(self, path):
        if os.path.exists(path):
            post = frontmatter.load(path)
            res = {}
            for key in post.keys():
                res[key] = post[key]
            return res
        else:
            return None

    def parse_path(self, path, encoded=True):
        if "/" in path:
            dir, filename = path.split("/")
            if encoded:
                dir = urllib.parse.quote(dir)
        else:
            dir, filename = "", path

        return dir, filename

    def page_content(self, path, encoded=True):
        parent, child = self.parse_path(path, encoded)

        if not self.sidebar.get(parent):

            raise Exception("Folder not found.")

        if self.sidebar[parent]["children"].get(child):
            dir = self.sidebar[parent]["children"][child]["dir"]
            filename = self.sidebar[parent]["children"][child]["filename"]
            path = f"{dir}/{filename}"
            return self.read_page_content(path)
        else:
            raise Exception("File not found.")

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
                    filename = get_filename(entry.name)
                    page = await self.read_page(f"{PAGES_DIR}/{dir}/{entry.name}")
                    if not page:
                        continue

                    id, title, parent, position = (
                        page.get("id"),
                        page.get("title"),
                        page.get("parent"),
                        page.get("position"),
                    )

                    if (
                        id == None
                        or title == None
                        or parent == None
                        or position == None
                    ):
                        continue

                    page["dir"] = dir
                    page["filename"] = filename
                    serialized_parent = get_parent_position(
                        str(parent), len(self.sidebar)
                    )

                    if self.sidebar.get(serialized_parent["id"]):
                        self.sidebar[serialized_parent["id"]]["children"][id] = page
                    else:
                        self.sidebar[serialized_parent["id"]] = {
                            "position": serialized_parent["position"],
                            "children": {id: page},
                            "title": parent,
                        }

    def get_template_data(self, path=None):
        if not path:
            # on route / renders the first page
            if len(self.sidebar) != 0:
                parent = list(self.sidebar.keys())[0]
                child = list(self.sidebar[parent]["children"].keys())[0]
            else:
                raise Exception(f"No files found in {PAGES_DIR}")
        else:
            parent, child = self.parse_path(path)

        path = f"{parent}/{child}"

        try:
            content = self.page_content(path, False)
        except Exception as e:
            raise Exception(str(e))

        res = {
            "title": "Patram",
            "current_dir": parent,
            "current_filename": child,
            "sidebar": self.sidebar,
            "content": content,
            "svg": self.get_logo(),
        }
        return res
