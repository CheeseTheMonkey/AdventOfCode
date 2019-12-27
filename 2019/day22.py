


def new_stack(deck):
    return deck[::-1]

def cut(deck, index):
    return deck[index:] + deck[:index]

def deal_with_increment(deck, increment):
    new_deck = [False] * len(deck)
    index = 0
    for card in deck:
        new_deck[index] = card
        index += increment
        index = index % len(deck)

    return new_deck

def shuffle(deck, instructions):
    for instruction in instructions:
        if instruction == "deal into new stack":
            deck = new_stack(deck)
        elif instruction.startswith("cut"):
            deck = cut(deck, int(instruction.split()[-1]))
        elif instruction.startswith("deal with increment"):
            deck = deal_with_increment(deck, int(instruction.split()[-1]))
    return deck


if __name__ == '__main__':
    instructions = [
        'deal with increment 7',
        'deal into new stack',
        'deal into new stack',
    ]
    assert(shuffle(list(range(10)), instructions) == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])

    instructions = [
        'cut 6',
        'deal with increment 7',
        'deal into new stack',
    ]
    assert(shuffle(list(range(10)), instructions) == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])

    instructions = [
        'deal into new stack',
        'cut -2',
        'deal with increment 7',
        'cut 8',
        'cut -4',
        'deal with increment 7',
        'cut 3',
        'deal with increment 9',
        'deal with increment 3',
        'cut -1',
    ]
    assert(shuffle(list(range(10)), instructions) == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])

    instructions = [a.strip() for a in open('day22.input').readlines()]

    print('Part 1:', shuffle(list(range(10007)), instructions).index(2019))

    # Part 2

    deck = list(range(119315717514047))
    for _ in range(101741582076661):
        deck = shuffle(deck, instructions)

    print("Part 2:", deck[2020])
