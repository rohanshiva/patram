parent_positions = {"1": 1, "": 0, "2": 2, "3": 3}


def get_parent_position(parent, parent_count):
    if parent_positions.get(parent) != None:
        return parent_positions.get(parent)
    else:
        return parent_count
