from collections import Counter
from common import read_input


def p1(lines: list[str]):
    l1, l2 = zip(*[item.split() for item in lines])
    print(f"Part1: {sum((abs(int(a)-int(b)) for a,b in zip(sorted(l1), sorted(l2))))}")


def p2(lines: list[str]):
    l1, l2 = zip(*[item.split() for item in lines])
    l2_count = Counter((int(a) for a in l2))
    print(f"Part2: {sum(int(a)*l2_count[int(a)] for a in l1)}")


def main():
    lines = read_input(1)
    p1(lines)
    p2(lines)
    

if __name__ == "__main__":
    main()