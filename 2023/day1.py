
from common import read_input


NUMBERS = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
)

def get_p1_value(line: str) -> int:
    digits = [char for char in line if char.isdigit()]
    return int(f'{digits[0]}{digits[-1]}')

def get_p2_value(line: str) -> int:
    l_indexes = {}
    r_indexes = {}
    for i in range(10):
        l_index = min((index for index in (len(line), line.find(str(i)), line.find(NUMBERS[i])) if index != -1))
        if l_index < len(line):
            l_indexes[l_index] = i
        r_index = max((-2, line.rfind(str(i)), line.rfind(NUMBERS[i])))
        if r_index > -1:
            r_indexes[r_index] = i

    return int(f'{l_indexes[min(l_indexes.keys())]}{r_indexes[max(r_indexes.keys())]}')


def main():
    lines = read_input(1)
    print(f'Part One: {sum(get_p1_value(line) for line in lines)}')
    print(f'Part Two: {sum(get_p2_value(line) for line in lines)}')

if __name__ == '__main__':
    main()