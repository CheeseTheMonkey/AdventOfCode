
from collections import namedtuple
from common import read_input
from dataclasses import dataclass, field
from typing import Optional
import sys

sys.setrecursionlimit(20000)


Coord = namedtuple('Coord', ['x', 'y'])

class NotConnectedError(Exception):
    pass


@dataclass
class Pipe:
    val: str
    location: Coord
    connections: list[Coord]

    def get_next_connection(self, from_loc: Coord):
        return [connection for connection in self.connections if connection != from_loc][0]

    def get_distance_to_start(self, grid, from_loc: Optional[Coord] = None):
        if self.val == 'S':
            return 0
        distances = []
        connections = [connection for connection in self.connections if connection in grid and connection != from_loc]
        if not connections:
            return -1
        
        for connection in connections:
            distances.append(grid[connection].get_distance_to_start(grid, self.location))
        
        actual_distances = [distance for distance in distances if distance != -1]
        if actual_distances:
            return min((distance for distance in actual_distances if distance != -1)) + 1
        return -1   

    def __repr__(self):
        return f"{self.val}: {self.location} - {self.connections}"     





def main():
    lines = read_input(10)
    grid: dict[Coord, Pipe] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.':
                continue

            loc = Coord(x,y)
            connections: list[Coord] = []
            if char in '|LJ' and y > 0:
                connections.append(Coord(x, y-1))
            if char in '-LF' and x < len(lines):
                connections.append(Coord(x+1, y))
            if char in '|7F' and y < len(lines):
                connections.append(Coord(x, y+1))
            if char in '-7J' and x > 0:
                connections.append(Coord(x-1, y))

            grid[loc] = Pipe(char, loc, connections)
            if char == 'S':
                start = grid[loc]
    for pipe in grid.values():
        if start.location in pipe.connections:
            start.connections.append(pipe.location)

    count = 1
    last_location = start.location
    location = start.connections[0]
    while location != start.location:
        location, last_location = grid[location].get_next_connection(last_location), location
        count += 1

    print(f"Part One: {count // 2}")
            

if __name__ == '__main__':
    main()