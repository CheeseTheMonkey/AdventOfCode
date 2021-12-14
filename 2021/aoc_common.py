
def read_file(filename):
    return open(filename).read().rstrip('\n')

def read_file_by_line(filename):
    return read_file(filename).split('\n')

def read_file_by_int(filename):
    return [int(a) for a in read_file_by_line(filename)]

def read_int_grid(filename):
    return [[int(a) for a in row] for row in read_file_by_line(filename)]

def read_int_grid_with_coords(filename):
    return {Coord(x, y): int(cell) for y, line in enumerate(read_file_by_line(filename)) for x, cell in enumerate(line)}

def print_grid(grid):
    for row in grid:
        print("".join((a and str(a) or "." for a in row)))

class Coord:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, coord):
        if not isinstance(coord, Coord):
            raise NotImplementedError
        return Coord(self.x + coord.x, self.y + coord.y)

    def __repr__(self):
        return f"Coord({self.x}, {self.y})"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, coord):
        if not isinstance(coord, Coord):
            raise TypeError
        return self.x == coord.x and self.y == coord.y

    def neighbours(self, diagonals=False):
        adj = [
            Coord(self.x - 1, self.y),
            Coord(self.x + 1, self.y),
            Coord(self.x, self.y - 1),
            Coord(self.x, self.y + 1)
        ]
        if diagonals:
            adj.extend([
                Coord(self.x - 1, self.y - 1),
                Coord(self.x - 1, self.y + 1),
                Coord(self.x + 1, self.y - 1),
                Coord(self.x + 1, self.y + 1)
            ])
        return adj
