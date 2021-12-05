

from aoc_common import read_file_by_line

def print_grid(grid):
    for row in grid:
        print("".join((a and str(a) or "." for a in row)))

def draw_lines(lines, grid, diagonals=False):
    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2 or diagonals:
            dx = x1 < x2 and 1 or x1 > x2 and -1 or 0
            dy = y1 < y2 and 1 or y1 > y2 and -1 or 0
            x, y = x1, y1
            while x != (x2 + dx) or y != (y2 + dy):
                grid[y][x] += 1
                x += dx
                y += dy

#data = read_file_by_line("day05.testinput")
data = read_file_by_line("day05.input")

max_x = 0
max_y = 0

lines = []
for row in data:
    p1, p2 = row.split(" -> ")
    p1 = [int(a) for a in p1.split(",")]
    p2 = [int(a) for a in p2.split(",")]
    max_x = max(p1[0], p2[0], max_x)
    max_y = max(p1[1], p2[0], max_y)
    lines.append([item for l in [p1, p2] for item in l])

grid = []
for _ in range(max_y + 1):
    grid.append([0] * (max_x + 1))

draw_lines(lines, grid)
print("Part 1: ", len([point for line in grid for point in line if point >= 2]))

grid = []
for _ in range(max_y + 1):
    grid.append([0] * (max_x + 1))

draw_lines(lines, grid, True)
print("Part 2: ", len([point for line in grid for point in line if point >= 2]))
