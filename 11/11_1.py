Node = tuple[str, list[str]]
NAME = 0
LINKS = 1


def find_node(graph: list[Node], name: str) -> Node:
    return next(n for n in graph if n[NAME] == name)


def get_num_paths(graph: list[Node], node: Node) -> int:
    paths = 0
    for link in node[LINKS]:
        if link == "out":
            paths += 1
        else:
            paths += get_num_paths(graph, find_node(graph, link))
    return paths


with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]
    nodes = [(l.split(":")[0], [n for n in l.split(":")[1].strip().split(" ")]) for l in lines]

start_node = find_node(nodes, "you")

print(get_num_paths(nodes, start_node))