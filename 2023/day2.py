from __future__ import annotations
from dataclasses import dataclass, field
from common import read_input


@dataclass
class Cubes:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other: Cubes):
        attrs = ['red', 'green', 'blue']
        return all((getattr(self, attr) <= getattr(other, attr) for attr in attrs))

    def __str__(self):
        return f'{Cubes.__name__}: {self.red} red, {self.green} green, {self.blue} blue'

    def power(self):
        return self.red * self.green * self.blue


class Hand(Cubes):

    @classmethod
    def from_hand_string(cls, hand: str) -> Hand:
        vals = hand.split(', ')
        cubes = cls()
        for val in vals:
            num, colour = val.split()
            setattr(cubes, colour, int(num))
        return cubes


@dataclass
class Game:
    game: str
    hands: list[Hand] = field(default_factory=list)

    @classmethod
    def from_game_line(self, game_line: str) -> Game:
        game, hands = game_line.split(': ')
        return Game(game, [Hand.from_hand_string(hand) for hand in hands.split('; ')])

    def game_number(self) -> int:
        return int(self.game.split()[1])

    def is_possible(self, cubes: Cubes) -> bool:
        return all((hand <= cubes for hand in self.hands))

    def min_cubes_needed(self) -> Cubes:
        return Cubes(
            max(
                (hand.red for hand in self.hands)
            ),
            max(
                (hand.green for hand in self.hands)
            ),
            max(
                (hand.blue for hand in self.hands)
            )
        )


def main():
    lines = read_input(2)
    bag = Cubes(12,13,14)
    total = 0
    powers = 0
    for line in lines:
        game = Game.from_game_line(line)
        if game.is_possible(bag):
            total += game.game_number()
        powers += game.min_cubes_needed().power()
            
    print(f"Part One: {total}")
    print(f"Part Two: {powers}")

if __name__ == '__main__':
    main()