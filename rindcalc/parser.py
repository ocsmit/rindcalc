import json
import re

INDEX_MAP = "./index_map.json"


def get_index(index_name):
    """

    :index_name: TODO
    :returns: TODO

    """
    with open(INDEX_MAP) as f:
        index_map = json.load(f)

    expression = index_map.get(index_name)
    if expression is None:
        raise Exception(f"No index of name {index_name}")

    return expression


def parse_index(expression):
    return re.findall("[\\w]*[\\s0-9] | [\\w]+", expression)


print(parse_index(get_index("ndvi")))
