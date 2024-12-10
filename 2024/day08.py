from common import read_input
from collections import defaultdict
from itertools import combinations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, change):
        return Point(self.x + change.x, self.y + change.y)

    def __sub__(self, change):
        return Point(self.x - change.x, self.y - change.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def get_tuple(self):
        return (self.x, self.y)


class Vector:
    def __init__(self, a: Point|int, b: Point|int):
        if isinstance(a, Point) and isinstance(b, Point):
            self.x = b.x - a.x
            self.y = b.y - a.y
        elif isinstance(a, int) and isinstance(b, int):
            self.x = a
            self.y = b
        else:
            raise ValueError

    def __mul__(self, multiple):
        return Vector(self.x * multiple, self.y * multiple)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


def inbounds(point: Point, max_x, max_y):
    return 0 <= point.x <= max_x and 0 <= point.y <= max_y


def p1(antennae: defaultdict[list[tuple]], max_i: int, max_j: int):
    antinodes = set()
    for nodes in antennae.values():
        for node1, node2 in combinations(nodes, 2):
            p1 = Point(*node1)
            vector = Vector(p1, Point(*node2))
            an1 = p1 - vector
            an2 = p1 + (vector * 2)
            for an in [an1, an2]:
                if inbounds(an, max_i, max_j):
                    antinodes.add(an.get_tuple())

    print(f"Part One: {len(antinodes)}")

            
def p2(antennae: defaultdict[list[tuple]], max_i: int, max_j: int):
    antinodes = set()
    for nodes in antennae.values():
        for node1, node2 in combinations(nodes, 2):
            p1 = Point(*node1)
            antinodes.add(node1)
            vector = Vector(Point(*node2), p1)

            current_position = p1
            while True:
                current_position += vector
                if not inbounds(current_position, max_i, max_j):
                    break
                antinodes.add(current_position.get_tuple())

            current_position = p1
            while True:
                current_position -= vector
                if not inbounds(current_position, max_i, max_j):
                    break
                antinodes.add(current_position.get_tuple())

    print(f"Part Two: {len(antinodes)}")


def day08():
    lines = read_input(8)
    antennae = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                antennae[c].append((i,j))
    max_i, max_j = i, j
    p1(antennae, max_i, max_j)
    p2(antennae, max_i, max_j)



if __name__ == "__main__":
    day08()