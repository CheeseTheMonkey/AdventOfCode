
from common import read_input
from itertools import pairwise


def get_next_number_in_sequence(sequence: list[int], forwards: bool= True) -> int:

    if all((num==0 for num in sequence)):
        return 0
    if forwards:
        return sequence[-1] + get_next_number_in_sequence(
            [b - a for a, b in pairwise(sequence)]
        )
    else:
        return sequence[0] - get_next_number_in_sequence(
            [b - a for a, b in pairwise(sequence)], False
        )


def main():
    oasis = read_input(9)
    sequences = [[int(a) for a in line.split()] for line in oasis]
    print(f"Part One: {sum([get_next_number_in_sequence(sequence) for sequence in sequences])}")
    print(f"Part Two: {sum([get_next_number_in_sequence(sequence, False) for sequence in sequences])}")
    


if __name__ == '__main__':
    main()