
from aoc_common import read_file_by_line


def count_paths(graph, may_dup=False):
    work = [(('start',), None)]
    paths = 0
    while work:
        path, dup = work.pop()
        if path[-1] == 'end':
            paths += 1
        else:
            for node in graph[path[-1]]:
                if node.isupper() or node not in path:
                    work.append((path + (node,), dup))
                elif may_dup and not dup and node != 'start':
                    work.append((path + (node,), node))
    return paths


data = [a.split('-') for a in read_file_by_line("day12.testinput")]
#data = [a.split('-') for a in read_file_by_line("day12.input")]

graph = {}
for a,b in data:
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

print(f"Part 1: {count_paths(graph)}")
print(f"Part 2: {count_paths(graph, True)}")
