
from common import read_input


def main():
    line = read_input(1)[0]
    floor = 0
    basement = 0
    for idx, char in enumerate(line, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1 and not basement:
            basement = idx

    print(f"Part One: {floor}")
    print(f"Part Two: {basement}")

if __name__ == '__main__':
    main()
