
from aoc_common import read_int_grid_with_coords, Coord



#octopuses = read_int_grid_with_coords("day11.testinput")
octopuses = read_int_grid_with_coords("day11.input")

def print_octopuses(octopuses):
    for i in range(10):
        line = ""
        for j in range(10):
            value = octopuses[Coord(j,i)]
            if value == 0:
                line += f"\033[1m{value}\033[0m"
            else:
                line += str(value)
        print(line)

print_octopuses(octopuses)
step, part1, part2 = 0, 0, 0

while step := step + 1:
    flashing, flashed = set(), set()
    for o in octopuses:
        octopuses[o] += 1
        if octopuses[o] > 9:
            flashing.add(o)

    while flashing:
        o = flashing.pop()
        flashed.add(o)
        octopuses[o] = 0

        for coord in o.neighbours(True):
            if coord in octopuses and coord not in flashed:
                octopuses[coord] += 1
                if octopuses[coord] > 9:
                    flashing.add(coord)

    if not part2 and len(flashed) == len(octopuses):
        part2 = step

    if step <= 100:
        part1 += len(flashed)
    elif part2:
        print("\n", step, "\n----------")
        print_octopuses(octopuses)
        break
    print("\n", step, "\n----------")
    print_octopuses(octopuses)

print("Part 1: ", part1)
print("Part 2: ", part2)
