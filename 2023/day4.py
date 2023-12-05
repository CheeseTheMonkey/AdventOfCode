
from common import read_input

def parse_numbers(numbers: str) -> list[int]:
    return [int(num) for num in numbers.split()]


def p1(cards: list[str]):
    total: int = 0
    scratchers = [1] * len(cards)
    for i, card in enumerate(cards):
        numbers = card.split(': ')[1]
        winners, have = [set(parse_numbers(nums)) for nums in numbers.split(' | ')]
        if matches := len(winners.intersection(have)):
            total += 2**(matches - 1)
            for j in range(matches):
                scratchers[i + j + 1] += scratchers[i]

    print(f"Part One {total}")
    print(f"Part Two {sum(scratchers)}")



def main():
    lines = read_input(4)
    p1(lines)

if __name__ == '__main__':
    main()