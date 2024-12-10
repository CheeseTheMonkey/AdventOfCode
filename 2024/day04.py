from collections import defaultdict
from common import read_input


D = -1, 0, 1


def p1(grid: defaultdict, coords: list[tuple]):
    target = list("XMAS")
    count = sum([grid[i+di*n, j+dj*n] for n in range(4)] == target for di in D for dj in D for i,j in coords)
    print(f"Part One: {count}")


def p2(grid: defaultdict, coords: list[tuple]):
    target = list("MAS"), list("SAM")
    count = sum([grid[i+d, j+d] for d in D] in target
            and [grid[i+d, j-d] for d in D] in target for i,j in coords)
    print(f"Part Two: {count}")


def day4():
    lines = read_input(4)
    grid = defaultdict(str) | {(i,j):c for i, r in enumerate(lines) for j, c in enumerate(r)}
    coords = list(grid.keys())
    p1(grid, coords)
    p2(grid, coords)


if __name__ == "__main__":
    day4()