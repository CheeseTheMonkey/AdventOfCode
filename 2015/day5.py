
from collections import Counter
from common import read_input
from itertools import groupby


def is_nice(value: str) -> bool:
    count = Counter(value)
    if sum((count[vowel] for vowel in 'aeiou')) < 3:
        return False
    if all((len(list(dups)) < 2 for _, dups in groupby(value))):
        return False
    if any((bad_string in value for bad_string in ['ab', 'cd', 'pq', 'xy'])):
        return False
    return True

def p2_is_nice(value: str) -> bool:
    if not any((value[i:i+2] in value[i+2:] for i in range(len(value) - 3))):
        return False
    if not any((value[i] == value[i + 2] for i in range(len(value) - 2))):
        return False
    return True


def main():
    strings = read_input(5)
    print(f"Part One: {sum(is_nice(value) for value in strings)}")
    print(f"Part One: {sum(p2_is_nice(value) for value in strings)}")


if __name__ == '__main__':
    main()