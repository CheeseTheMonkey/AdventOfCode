

from collections import namedtuple
from common import read_input
from typing import Iterator


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

EMPTY = "."
HSPLIT = "-"
VSPLIT = "|"
MIRROR_FW = "/"
MIRROR_BW = "\\"


BeamPath = namedtuple('BeamPath', ['x', 'y', 'dir'])


class BeamMapper:
    def __init__(self, grid: list[list[str]], start: BeamPath):
        self._grid = grid
        self._width = len(grid[0])
        self._height = len(grid)
        self.energised: set[BeamPath] = set()
        self.start = start

    def trace_beam(self):
        beams = [self.start]
        while beams:
            beam = beams.pop()
            if beam not in self.energised and 0 <= beam.x < self._width and 0 <= beam.y < self._height:
                self.energised.add(beam)
                beams.extend(self.next_tiles(beam))


    def _get_neighbour(self, beam: BeamPath) -> BeamPath:
        # Assume x,y is in the layout's boundaries
        if beam.dir == NORTH:
            if beam.y > 0:
                return BeamPath(beam.x, beam.y - 1, beam.dir)
        elif beam.dir == EAST:
            if beam.x + 1 < self._width:
                return BeamPath(beam.x + 1, beam.y, beam.dir)
        elif beam.dir == SOUTH:
            if beam.y + 1 < self._height:
                return BeamPath(beam.x, beam.y + 1, beam.dir)
        elif beam.dir == WEST:
            if beam.x > 0:
                return BeamPath(beam.x - 1, beam.y, beam.dir)

    def next_tiles(self, beam:BeamPath) -> Iterator[BeamPath]:
        tile = self._grid[beam.y][beam.x]
        if tile == EMPTY:
            if neighbour := self._get_neighbour(beam):
                yield neighbour
        elif tile == MIRROR_BW:
            to = {NORTH: WEST, EAST: SOUTH, SOUTH: EAST, WEST: NORTH}[beam.dir]
            if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, to)):
                yield neighbour
        elif tile == MIRROR_FW:
            to = {NORTH: EAST, EAST: NORTH, SOUTH: WEST, WEST: SOUTH}[beam.dir]
            if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, to)):
                yield neighbour
        elif tile == HSPLIT:
            if dir in [EAST, WEST]:
                if neighbour := self._get_neighbour(beam):
                    yield neighbour
            else:
                if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, EAST)):
                    yield neighbour
                if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, WEST)):
                    yield neighbour
        elif tile == VSPLIT:
            if dir in [NORTH, SOUTH]:
                if neighbour := self._get_neighbour(beam):
                    yield neighbour
            else:
                if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, NORTH)):
                    yield neighbour
                if neighbour := self._get_neighbour(BeamPath(beam.x, beam.y, SOUTH)):
                    yield neighbour

    def get_energised_cells(self) -> int:
        return len(set((beam.x, beam.y) for beam in self.energised))


def test_all_beam_mappings(grid: list[list[str]]) -> int:
    energised = []
    for i in range(len(grid)):
        mapper = BeamMapper(grid, BeamPath(0, i, EAST))
        mapper.trace_beam()
        energised.append(mapper.get_energised_cells())
        mapper = BeamMapper(grid, BeamPath(len(grid[0]) - 1, i, WEST))
        mapper.trace_beam()
        energised.append(mapper.get_energised_cells())
    for i in range(len(grid[0])):
        mapper = BeamMapper(grid, BeamPath(i, 0, SOUTH))
        mapper.trace_beam()
        energised.append(mapper.get_energised_cells())
        mapper = BeamMapper(grid, BeamPath(i, len(grid) - 1, NORTH))
        mapper.trace_beam()
        energised.append(mapper.get_energised_cells())

    return max(energised)


def main():
    grid = [list(line) for line in read_input(16)]

    mapper = BeamMapper(grid, BeamPath(0, 0, 1))
    mapper.trace_beam()
    print(f"Part One: {mapper.get_energised_cells()}")
    print(f"Part Two: {test_all_beam_mappings(grid)}")


if __name__ == '__main__':
    main()