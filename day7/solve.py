import re


PARENT_REGEX = re.compile('^(.*) bags$')
CHILD_REGEX = re.compile('^(\d+) (.*) bags?.?$')


def get_parent(part):
    return PARENT_REGEX.match(part.strip())[1]


def get_child(part):
    match = CHILD_REGEX.match(part.strip())
    return int(match[1]), match[2]


def parse_line(line):
    p, c = line.split('contain')
    parent = get_parent(p)

    children = []
    if c.strip() == 'no other bags.':
        return parent, children
    
    for child in c.split(','):
        children.append(get_child(child))

    return parent, children


def build_graph(input):
    graph = {}
    for line in input:
        parent, children = parse_line(line)
        graph[parent] = children
    return graph


def count_all_bags(target, graph, visited={}):
    if target in visited:
        return visited[target]

    total = 1
    for child in graph[target]:
        total += child[0] * count_all_bags(child[1], graph, visited)
    
    visited[target] = total
    return total


def solve(input):
    graph = build_graph(input)
    return count_all_bags('shiny gold', graph) - 1
