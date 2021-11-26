import os
import json
import markdown
from collections import defaultdict

PAGES_PATH = "./pages"


def deserialize(key, type="FILE"):
    if not key:
        return key
    if type == "FILE":
        words = key.split(".md")[0].split("-")
    else:
        words = key.split("-")
    for i, word in enumerate(words):
        words[i] = word.title()
    return " ".join(words)


def serialize(key):
    words = key.split(" ")
    for i, word in enumerate(words):
        words[i] = word[0].lower() + word[1:]

    res = "-".join(words)
    return res


def get_file(path):
    if (os.path.exists(path)):
        f = open(path)
        content = f.read()
        f.close()
        return content
    else:
        return None


class Crawler:
    def __init__(self):
        self.__sidebar = defaultdict(lambda: [])
        self.__crawl()
        self.__metadata = self.__crawl_metadata()

    def __crawl_metadata(self):
        try:
            f = open("metadata.json")
            data = json.load(f)
            f.close()
            return data
        except:
            return None

    def __crawl(self, dir=""):
        with os.scandir(f"{PAGES_PATH}/{dir}") as expected_entries:
            for entry in expected_entries:
                if entry.is_dir():
                    self.__crawl(entry.name)
                else:
                    self.__sidebar[deserialize(dir, type="DIR")].append(
                        deserialize(entry.name))

    def get_sidebar(self):
        return self.__sidebar

    def page_content(self, path="README"):
        path = f"{PAGES_PATH}/{path}.md"
        raw_content = get_file(path)
        if raw_content:
            return markdown.markdown(str(raw_content))

    def preload_headers(self):
        res = []
        for dir in self.__sidebar:
            for page in self.__sidebar[dir]:
                if dir == "":

                    serialized_page = serialize(page)
                    path = f"/raw/{serialized_page}"
                else:

                    serialized_dir = serialize(dir)
                    serialized_page = serialize(page)
                    path = f"/raw/{serialized_dir}/{serialized_page}"
                res.append(path)
        return res

    def get_template_data(self, path=None):
        if path:
            page_content = self.page_content(path)
            key = path.split("/")[1]
            key = deserialize(f"{key}.md")
        else:
            page_content = self.page_content()
            key = "README"

        res = {"title": self.__metadata["title"], "key": key,
               "sidebar": self.__sidebar, "nav_links": self.__metadata["nav_links"], "header_tags": self.preload_headers()}

        root_pages = res["sidebar"].get("")
        if root_pages:
            root_pages = {"": root_pages}
            del res["sidebar"][""]
            root_pages.update(res["sidebar"])
            res["sidebar"] = root_pages

        res["note"] = page_content
        res["path"] = path
        return res
