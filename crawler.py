import os
from highlight_renderer import markdown

PAGES_DIR = "./pages"


def get_filename(entry_name):
    return entry_name[:-3]


def serialize(entry_name, folder=False):
    if entry_name == "":
        return {"position": 0, "name": "", "raw": ""}

    parts = entry_name.split("-")

    name = " ".join(map(lambda word: word[0].upper() + word[1:], parts[1:]))
    name = name
    raw_name = "-".join(parts[1:])
    if not folder:
        name = get_filename(name)
        raw_name = get_filename(raw_name)
    try:
        return {"position": int(parts[0].strip()), "name": name, "raw": raw_name}
    except BaseException as e:
        pass


def deserialize(entry_name, folder=False):
    parts = entry_name.split(" ")
    if entry_name == "":
        return ""

    res = "-".join(map(lambda word: word[0].lower() + word[1:], parts))
    if folder:
        return res
    else:
        return f"{res}.md"


class Crawler:
    def __init__(self):
        """
        Sample Sidebar
        {
            "folder-one": {
                "position": 1,
                "name": "Folder One",
                "children": { "doc-one": { "position": 1, "name": "Doc One" } }
            }
        }
        """
        self.sidebar = {}

    async def setup(self):
        await self.build()
        # rearrange sidebar according to position
        await self.sort_sidebar()

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

    def read_page(self, path):
        if os.path.exists(path):
            f = open(path, encoding="utf8")
            raw_content = f.read()
            f.close()
            return markdown(raw_content)
        else:
            return None

    def parse_path(self, path):
        if "/" in path:
            dir, filename = path.split("/")
        else:
            dir, filename = "", path

        res = []
        if dir == "" and self.sidebar.get(dir):
            res.append("")
        elif self.sidebar.get(dir):
            res.append(f"{self.sidebar[dir]['position']}-{dir}")
        else:
            raise Exception("Folder not found.")

        if self.sidebar[dir]["children"].get(filename):
            res.append(
                f"{self.sidebar[dir]['children'][filename]['position']}-{filename}"
            )
        else:
            raise Exception("File not found in the directory.")

        return res

    async def build(self, dir=""):
        with os.scandir(f"{PAGES_DIR}/{dir}") as entries:
            for entry in entries:
                if entry.is_dir():
                    if len(os.listdir(f"{PAGES_DIR}/{entry.name}")) > 0:
                        await self.build(entry.name)
                else:

                    if not entry.name.endswith(".md"):
                        continue

                    serialized_dir = serialize(dir, folder=True)
                    serialized_file = serialize(entry.name)

                    if self.sidebar.get(serialized_dir["raw"]):
                        dir_position = self.sidebar[serialized_dir["raw"]]["position"]
                        if serialized_dir["position"] == dir_position:
                            self.sidebar[serialized_dir["raw"]]["children"][
                                serialized_file["raw"]
                            ] = {
                                "position": serialized_file["position"],
                                "name": serialized_file["name"],
                            }
                    else:
                        self.sidebar[serialized_dir["raw"]] = {
                            "position": serialized_dir["position"],
                            "name": serialized_dir["name"],
                            "children": {
                                serialized_file["raw"]: {
                                    "position": serialized_file["position"],
                                    "name": serialized_file["name"],
                                }
                            },
                        }

    def page_content(self, path):
        if not path:
            return markdown(f"Add some docs in {PAGES_DIR}/ folder, and check back here") 

        try:
            dir, filename = self.parse_path(path)
        except Exception as e:
            raise Exception(str(e))

        path = f"{PAGES_DIR}/{dir}/{filename}.md"

        content = self.read_page(path)
        if content != None:
            return content
        else:
            raise Exception("File not found.")

    def get_template_data(self, path=None):
        if not path:
            # on / route renders the first page
            if len(self.sidebar) > 0:
                dir = list(self.sidebar.keys())[0]
                filename = list(self.sidebar[dir]["children"].keys())[0]
                path = f"{dir}/{filename}"
            else:
                path = None

        try:
            content = self.page_content(path)
        except Exception as e:
            raise Exception(str(e))

        dir, filename = "", ""
        if path:
            dir, filename = "", path
            if "/" in path:
                dir, filename = path.split("/")

        res = {
            "title": "Patram",
            "current_dir": dir,
            "current_filename": filename,
            "sidebar": self.sidebar,
            "content": content,
        }

        return res
