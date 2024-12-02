
from common import read_input
from dataclasses import dataclass
from itertools import groupby
from tqdm import tqdm


@dataclass
class Map:
    dest_start: int
    source_start: int
    length: int

    def map(self, location):
        if location in range(self.source_start, self.source_end):
            return location - self.source_start + self.dest_start
        return location

    @property
    def source_end(self):
        return self.source_start + self.length

    @property
    def dest_end(self):
        return self.dest_start + self.length
    
    def reverse_map(self, location):
        if location in range(self.dest_start, self.dest_start):
            return location - self.dest_start + self.source_start
        return location


@dataclass
class FullMap:
    _map: list[Map]

    def __init__(self, maps):
        self._map = []
        _maps = maps.split('x')
        for map in _maps:
            self._map.append(Map(*[int(a) for a in map.split()]))


    def map(self, location):
        orig_loc = location
        for map in self._map:
            location = map.map(location)
            if location != orig_loc:
                return location
        return location

    def reverse_map(self, endpoint):
        startpoint = endpoint
        for map in self._map:
            startpoint = map.reverse_map(startpoint)
            if startpoint != endpoint:
                return startpoint
        return startpoint

def main():
    lines = read_input(5)
    input_data = ['x'.join(list(g)) for k, g in groupby(lines, key=bool) if k]
    seeds = [int(num) for num in input_data[0].split(': ')[1].split()]
    maps = [
        FullMap(maps) for _, maps in [x.split(':x') for x in input_data[1:]]
    ]
    locations = seeds
    for map in maps:
        locations = [map.map(location) for location in locations]
    print(f"Part One: {min(locations)}")

    location = 503300000
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    while True:
        done = False
        if not location % 1000000:
            print(location)
        endpoint = location
        for map in maps[::-1]:
            endpoint = map.reverse_map(endpoint)
        for begin, end in seed_ranges:
            if begin <= endpoint <= end:
                print(f"Part Two: {endpoint}")
                done = True
                break

        if done == True:
            break
        location += 1

if __name__ == '__main__':
    main()