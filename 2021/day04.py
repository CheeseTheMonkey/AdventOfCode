from aoc_common import read_file
from operator import itemgetter

def apply_call(boards, call):
    return [[['x' if i == call else i for i in line] for line in board] for board in boards]

def has_won(boards):
    return sorted([(board, idx) for idx, board in enumerate(boards) if (any(all(i == "x" for i in line) for line in board) or
                                          any(all(line[index] == "x" for line in board) for index in range(len(board[0]))))],
                  key=itemgetter(1), reverse=True)

def score(board, call):
    return sum(i for line in board for i in line if i != 'x') * call

#calls, *boards = read_file("day04.testinput").split("\n\n")
calls, *boards = read_file("day04.input").split("\n\n")

calls = [int(i) for i in calls.split(",")]
boards = [[[int(i) for i in line.split()] for line in board.split('\n')] for board in boards]


firstWon = False
for call in calls:
    boards = apply_call(boards, call)

    if winning_boards := has_won(boards):
        if not firstWon:
            assert(len(winning_boards) == 1)
            print("Part 1: ", score(winning_boards[0][0], call))
            firstWon = True
        if len(boards) == 1:
            assert(len(winning_boards) == 1)
            print("Part 2: ",score(winning_boards[0][0], call))


        for _, idx in winning_boards:
            del boards[idx]
