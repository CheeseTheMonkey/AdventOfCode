
from common import read_input
from dataclasses import dataclass
from math import prod


@dataclass
class Dimensions:
    l: int
    w: int
    d: int

    def smallest_dimensions(self) -> (int, int):
        dims = sorted([self.l, self.w, self.d])
        return dims[0], dims[1]

    def smallest_surface(self) -> int:
        return prod(self.smallest_dimensions()) 

    def wrapping(self) -> int:
        return 2 * self.l * self.w + 2 * self.l * self.d + 2 * self.w * self.d + self.smallest_surface()
    
    def ribbon(self) -> int:
        dims = self.smallest_dimensions()
        return dims[0]*2 + dims[1]*2 + (self.l * self.w * self.d)


def main():
    lines = read_input(2)
    square_footage = 0
    ribbon = 0
    for line in lines:
        dims = Dimensions(*[int(dim) for dim in line.split('x')])
        square_footage += dims.wrapping()
        ribbon += dims.ribbon()
    print(f"Part One:  {square_footage}")
    print(f"Part Two:  {ribbon}")
        

if __name__ == '__main__':
    main()