
from common import read_input
from collections import namedtuple


Coord = namedtuple('Coord', ['x', 'y'])

def mod_x_y(char: str, x: int, y: int) -> (int, int):
        if char == '<':
            x -= 1
        elif char == '>':
            x += 1
        elif char == 'v':
            y -= 1
        elif char == '^':
            y += 1
        return (x, y)


def main():
    line = read_input(3)[0]
    x, y = 0, 0
    robo_x, robo_y = 0, 0
    santa_x, santa_y = 0, 0
    houses = {Coord(x, y)}
    robo = {Coord(x, y)}
    santa = {Coord(x, y)}
    for idx, char in enumerate(line):
        x, y = mod_x_y(char, x, y)
        houses.add(Coord(x, y))
        if idx % 2:
            robo_x, robo_y = mod_x_y(char, robo_x, robo_y)
            robo.add(Coord(robo_x, robo_y))
        else:
            santa_x, santa_y = mod_x_y(char, santa_x, santa_y)
            santa.add(Coord(santa_x, santa_y))

    print(f"Part One: {len(houses)}")

    print(f"Part Two: {len(robo.union(santa))}")


if __name__ == '__main__':
    main()