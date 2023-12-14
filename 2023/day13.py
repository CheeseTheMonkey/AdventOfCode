

from common import read_input
from itertools import groupby


def get_rows_above_symmetry_line(grid: list[str]) -> int:
    for i in range(len(grid)):
        split = list(zip(grid[i+1:], grid[i::-1]))
        if split and all((a == b for a, b in split)):
            return i + 1
    return 0

def get_columns_left_of_symmetry_line(grid: list[str]) -> int:
    # Flip the axes, then use the above method...    
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    return get_rows_above_symmetry_line(grid)


def p1(grids: list[list[str]]) -> int:
    ret = 0
    for grid in grids:
        ret += get_columns_left_of_symmetry_line(grid)
        ret += (100 * get_rows_above_symmetry_line(grid))

    return ret


def main():
    lines = read_input(13)
    grids = [list(line) for line in [list(g) for k, g in groupby(lines, key=bool) if k]]
    print(f"Part One: {p1(grids)}")
        

if __name__ == '__main__':
    main()
