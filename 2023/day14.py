

from collections import Counter
from common import read_input
from pprint import pprint
from tqdm import tqdm


def tilt(grid: list[str]) -> list[str]:
    
    return_grid = []
    for row in grid:
        sections = [''.join(sorted(section, reverse=True)) for section in row.split('#')]
        return_grid.append('#'.join(sections))
    
    return return_grid


def tilt_north(grid: list[str]) -> list[str]:
    # rotate so "North" is left
    grid = [''.join(i) for i in zip(*grid)]

    # rotate back to original orientation
    return [''.join(i) for i in zip(*tilt(grid))]


def tilt_west(grid: list[str]) -> list[str]:
    # No tilt needed on this one
    return tilt(grid)


def tilt_south(grid: list[str]) -> list[str]:
    # rotate so "South" is left
    grid = [''.join(i) for i in zip(*grid[::-1])]

    # rotate back to original orientation
    return [''.join(i) for i in zip(*tilt(grid))][::-1]


def tilt_east(grid: list[str]) -> list[str]:
    # flip so "East" is to the left
    grid = [row[::-1] for row in grid]
    
    return [row[::-1] for row in tilt(grid)]


def spin(grid: list[str]) -> list[str]:
    return tilt_east(tilt_south(tilt_west(tilt_north(grid))))
    

def get_load(grid: list[str]) -> int:
    total = 0
    for i, row in enumerate(grid):
        c = Counter(row)
        total += c['O'] * (len(grid) - i)

    return total


def main():
    grid = read_input(14)
    grid = tilt_north(grid)
    print(f"Part One: {get_load(grid)}")

    orig_grid = grid
    grids = []
    for i in tqdm(range(1000000000)):
        grid = spin(grid)
        if grid in grids:
            break
        grids.append(grid)
    
    idx = grids.index(grid)
    cycle_length = i - idx
    offset = (999999999 - i) % cycle_length

    print(f"Part Two: {get_load(grids[idx + offset])}")



if __name__ == '__main__':
    main()