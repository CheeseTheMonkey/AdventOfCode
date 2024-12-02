

from common import read_input
from itertools import groupby


def get_rows_above_symmetry_line(grid: list[str], expected_errors: int=0) -> int:
    # get the original line of reflection
    orig = -1
    if expected_errors != 0:
        orig = get_rows_above_symmetry_line(grid)

    for i in range(len(grid)):
        split = list(zip(grid[i+1:], grid[i::-1]))
        errors = 0
        if split:
            for a, b in split:
                if a != b:
                    errors += 1
                if errors > expected_errors:
                    break
            if errors == expected_errors and i + 1 != orig:
                return i + 1
    return 0

def get_columns_left_of_symmetry_line(grid: list[str], expected_errors: int=0) -> int:
    # Flip the axes, then use the above method...    
    grid = [''.join([row[i] for row in grid]) for i in range(len(grid[0]))]
    return get_rows_above_symmetry_line(grid, expected_errors)


def p1(grids: list[list[str]]) -> int:
    ret = 0
    for grid in grids:
        ret += get_columns_left_of_symmetry_line(grid)
        ret += (100 * get_rows_above_symmetry_line(grid))

    return ret


def p2(grids: list[list[str]]) -> int:
    ret = 0
    for grid in grids:
        ret += get_columns_left_of_symmetry_line(grid, 1)
        ret += (100 * get_rows_above_symmetry_line(grid, 1))

    return ret


def main():
    lines = read_input(13)
    grids = [list(line) for line in [list(g) for k, g in groupby(lines, key=bool) if k]]
    print(f"Part One: {p1(grids)}")
    print(f"Part Two: {p2(grids)}")
        

if __name__ == '__main__':
    main()
