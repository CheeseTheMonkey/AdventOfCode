
from collections import namedtuple
from common import read_input
from dataclasses import dataclass
from math import prod


Coord = namedtuple('Coord', ['x', 'y'])


@dataclass
class Number:
    number: int
    start: Coord
    end: Coord

    def y_range(self) -> tuple[int, int]:
        return (self.start.y - 1, self.end.y + 2)

    def x_range(self) -> tuple[int, int]:
        return (self.start.x - 1, self.end.x + 2)


@dataclass
class Symbol:
    coord: Coord
    symbol: str = "*"

    def is_adjacent_to_number(self, number: Number) -> bool:
        if self.coord.y in range(*number.y_range()) and self.coord.x in range(*number.x_range()):
            return True
        return False


def adjacent_to_symbol(start: Coord, end: Coord, lines: list[str]) -> bool:
    min_y = max((0, start.y - 1))
    max_y = min((len(lines) - 1, end.y + 2))
    min_x = max((0, start.x - 1))
    max_x = min((len(lines[0]) - 1, end.x + 2))

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            char = lines[y][x]
            if char != '.' and not char.isdigit():
                return True
    
    return False



def main():
    lines = read_input(3)
    total = 0
    numbers: list[Number] = []
    gears: list[Symbol] = []
    for y, line in enumerate(lines):
        num: str = ""
        start: Coord|None = None
        for x, val in enumerate(line):
            if val.isdigit():
                num += val
                if not start:
                    start = Coord(x, y)
                if x != len(line) - 1:
                    continue
            if start:
                end = Coord(x-1, y)
                numbers.append(Number(int(num), start, end))
                if adjacent_to_symbol(start, end, lines):
                    total += int(num)
                num = ""
                start = None
            if val == "*":
                gears.append(Symbol(Coord(x, y)))
        
    print(f"Part One: {total}")
    ratio: int = 0
    for gear in gears:
        adjacent: list[Number] = []
        for number in numbers:
            if gear.is_adjacent_to_number(number):
                adjacent.append(number)
        if len(adjacent) == 2:
            ratio += prod((number.number for number in adjacent))
    
    print(f"Part Two: {ratio}")



if __name__ == '__main__':
    main()