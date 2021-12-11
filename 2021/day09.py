
from aoc_common import read_int_grid, read_int_grid_with_coords
from math import prod


def find_basin(coord, height_map, visited=None):
    if visited == None:
        visited = set()
    visited.add(coord)

    for neighbour in coord.neighbours():
        if (neighbour in visited or neighbour not in height_map or height_map[neighbour] == 9
                                or height_map[neighbour] < height_map[coord]):
            continue
        visited.union(find_basin(neighbour, height_map, visited))

    return visited


#height_map = read_int_grid_with_coords("day09.testinput")
height_map = read_int_grid_with_coords("day09.input")

mins = []
risk_level = 0
basins = []

for coord, height in height_map.items():
    if any(neighbour in height_map and height_map[neighbour] <= height for neighbour in coord.neighbours()):
        continue

    risk_level += height + 1
    mins.append(coord)

for low in mins:
    basins.append(find_basin(low, height_map))

part2 = prod(len(basin) for basin in sorted(basins, key=len)[-3:])

print("Part 1: ", risk_level)
print("Part 2: ", part2)
