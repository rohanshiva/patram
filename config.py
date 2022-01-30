import urllib

parent_positions = {
    "1": {"id": "one", "position": 1},
    "": {"id": "", "position": 0},
    "Easy Stuff": {"id": "easy-stuff", "position": 2},
}


def get_parent_position(parent, parent_count):
    if parent_positions.get(parent) != None:
        return parent_positions.get(parent)
    else:
        return {"id": urllib.parse.quote(parent), "position": parent_count}
