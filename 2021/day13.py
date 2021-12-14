
from aoc_common import read_file, Coord
from copy import deepcopy
from operator import attrgetter


#coords, folds = read_file("day13.testinput").split("\n\n")
coords, folds = read_file("day13.input").split("\n\n")

grid = {Coord(x,y) for x, y in (line.split(',') for line in coords.split())}

part1 = False
for fold in folds.split("\n"):
    axis, value = fold.split()[-1].split('=')
    value = int(value)
    print(f"Folding along {axis}: {value}")
    new_grid = set()
    if axis == "y":
        for coord in grid:
            if coord.y > value:
                new_grid.add(Coord(coord.x, coord.y - (2 * (coord.y - value))))
            else:
                new_grid.add(coord)
    elif axis == "x":
        for coord in grid:
            if coord.x > value:
                new_grid.add(Coord(coord.x - (2 * (coord.x - value)), coord.y))
            else:
                new_grid.add(coord)
    grid = new_grid
    if not part1:
        print(f"Part 1: {len(grid)})")
        part1 = True

max_x = max(a.x for a in grid) + 1
max_y = max(a.y for a in grid) + 1

output = ""
for y in range(max_x):
    for x in range(max_x):
        if Coord(x, y) in grid:
            output += "#"
        else:
            output += "."
    output += "\n"

print(f"Part 2:\n{output}")

