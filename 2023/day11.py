
from collections import namedtuple
from common import read_input
from dataclasses import dataclass
from itertools import combinations
from tqdm import tqdm


Coord = namedtuple('Coord', ['x', 'y'])


@dataclass
class Star:
    loc: Coord

    @staticmethod
    def _expand_count(start: int, end: int, vals: list[int], factor: int) -> int:
        diff = abs(start - end)
        low = min(start, end) + 1
        high = max(start, end)
        empties = set(range(low, high)).intersection(set(vals))
        diff += (factor - 1) * len(empties)
        return diff

    def distance_to(self, other) -> int:
        return abs(self.loc.x - other.loc.x) + abs(self.loc.y - other.loc.y)

    def distance_to_with_expansion(self, other, columns: list[int], rows: list[int], factor=2) -> int:
        return self._expand_count(self.loc.x, other.loc.x, columns, factor) + \
               self._expand_count(self.loc.y, other.loc.y, rows, factor)


    def __repr__(self):
        return f"Star({self.loc.x}, {self.loc.y})"


def expand_grid(start_grid: list[list[str]]) -> list[list[str]]:
    """
    Return grid with additional empty rows
    """
    grid = []
    for row in start_grid:
        if all((char == '.' for char in row)):
            grid.extend([row] * 2)
        else:
            grid.append(row)

    return grid

def populate_grid(start_grid: list[list[str]]) -> list[list[str]]:
    """
    Expand rows and columns by flipping axes
    """
    # Expand the grid, then flip axes
    grid = expand_grid(start_grid)
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    
    # Same again, to get us back to the right orientation
    grid = expand_grid(grid)
    return [[row[i] for row in grid] for i in range(len(grid[0]))]


def get_stars(grid: list[list[str]]) -> list[Star]:

    stars: list[Star] = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                stars.append(Star(Coord(x,y)))
    return stars

def get_empty_rows(grid: list[list[str]]) -> list[int]:
    rows: list[int] = []
    for idx in range(len(grid)):
        if all((char == '.' for char in grid[idx])):
            rows.append(idx)
    return rows

def get_empty_columns(grid: list[list[str]]) -> list[int]:
    columns: list[int] = []
    for idx in range(len(grid[0])):
        if all((char == '.' for char in (line[idx] for line in grid))):
            columns.append(idx)
    return columns

def main():
    lines = [list(line) for line in read_input(11)]
    # Create grid with additional rows
    grid = populate_grid(lines)
    stars = get_stars(grid)

    print(f"Part One: {sum((a.distance_to(b) for a, b in combinations(stars, 2)))}")

    stars = get_stars(lines)
    columns = get_empty_columns(lines)
    rows = get_empty_rows(lines)
    print(f"Part Two: {sum((a.distance_to_with_expansion(b, columns, rows, 1000000) for a,b in combinations(stars, 2)))}")



if __name__ == '__main__':
    main()