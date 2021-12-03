
from aoc_common import read_file_by_line
from math import prod


class Position:
    def __init__(self):
        self._x = 0
        self._y = 0

    def navigate(self, data):
        for direction, magnitude in data:
            if not isinstance(magnitude, int):
                magnitude = int(magnitude)
            getattr(self, direction)(magnitude)

    def forward(self, magnitude):
        self._x += magnitude

    def backward(self, magnitude):
        self._x -= magnitude

    def down(self, magnitude):
        self._y += magnitude

    def up(self, magnitude):
        self._y -= magnitude

    def get_location(self):
        return (self._x, self._y)

    def print_position(self):
        print(self._x, self._y)

class AimedPosition(Position):
    def __init__(self):
        super().__init__()
        self._aim = 0

    def forward(self, magnitude):
        self._x += magnitude
        self._y += magnitude * self._aim

    def down(self, magnitude):
        self._aim += magnitude

    def up(self, magnitude):
        self._aim -= magnitude

    def print_position(self):
        print(self._x, self._y, self._aim)

#data = [line.split() for line in read_file_by_line("day02.testinput")]
data = [line.split() for line in read_file_by_line("day02.input")]


position = Position()
position.navigate(data)
print(prod(position.get_location()))

aimed_position = AimedPosition()
aimed_position.navigate(data)
print(prod(aimed_position.get_location()))
