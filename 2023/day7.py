
from collections import Counter
from common import read_input
from dataclasses import dataclass, field
from functools import total_ordering


@dataclass
class Card:
    _VALUES = ["2", "3", "4", "5", "6", "7", "8",
               "9", "T", "J", "Q", "K", "A"]
    value: str

    def __gt__(self, other):
        return self._VALUES.index(self.value) > self._VALUES.index(other.value)

    def __eq__(self, other):
        return self._VALUES.index(self.value) == self._VALUES.index(other.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(repr(self.value))


class JokerCard(Card):
    _VALUES = ["J", "2", "3", "4", "5", "6", "7",
               "8", "9", "T", "Q", "K", "A"]
    value: str
    


@dataclass
@total_ordering
class Hand:
    cards: list[Card] = field(default_factory=list)
    jokers: bool = False

    def __init__(self, hand_str:str, jokers: bool= False):
        self.cards = []
        self.jokers = jokers
        card_class = JokerCard if jokers else Card
        for char in hand_str:
            self.cards.append(card_class(char))

    def __str__(self):
        return f"Hand: {''.join((card.value for card in self.cards))}"

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if self.type() > other.type():
            return True
        elif self.type() == other.type():
            for a, b in zip(self.cards, other.cards):
                if a > b:
                    return True
                elif a < b:
                    return False
        return False

    def type(self):
        """
        Use to determine what type of hand we have ranked from 0 (highest card) to 6(five of a kind)
        """
        counts = Counter(self.cards)
        if self.jokers:
            joker = JokerCard("J")
            joker_count = counts[joker]
            del counts[joker]
        try:
            most, second = [count[1] for count in counts.most_common(2)]
            if self.jokers:
                most += joker_count
        except ValueError:
            # Only one entry in the counter, so it must be 5 of a kind
            return 6
        if most == 1:
            return 0
        if most == 2:
            if second == 1:
                return 1
            elif second == 2:
                return 2
        if most == 3:
            if second != 2:
                return 3
            elif second == 2:
                return 4
        if most == 4:
            return 5
        if most == 5:
            return 6
        raise AttributeError(f"something weird {most, second, counts[joker], self}")


def main():
    hands = [(Hand(hand), int(bid)) for hand, bid in [line.split() for line in read_input(7)]]
    hands.sort(key=lambda x: x[0])
    print(f"Part One: {sum((i * bid for i, (_, bid) in enumerate(hands, start=1)))}")

    joker_hands = [(Hand(hand, jokers=True), int(bid)) for hand, bid in [line.split() for line in read_input(7)]]
    joker_hands.sort(key=lambda x: x[0])
    print(f"Part Two: {sum((i * bid for i, (_, bid) in enumerate(joker_hands, start=1)))}")



if __name__ == '__main__':
    main()