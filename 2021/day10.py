

from aoc_common import read_file_by_line
from queue import LifoQueue


scores = {
    '>': 25137,
    ']': 57,
    '}': 1197,
    ')': 3
}

ac_scores = {
    '>': 4,
    ']': 2,
    '}': 3,
    ')': 1
}

matches = {
    '>': '<',
    ']': '[',
    '}': '{',
    ')': '('
}
r_matches = {v: k for k, v in matches.items()}


#data = read_file_by_line("day10.testinput")
data = read_file_by_line("day10.input")


score = 0
autocomplete_scores = []
for i, line in enumerate(data):
    queue = LifoQueue()
    for char in line:
        if char in ['<', '[', '{', '(']:
            queue.put(char)
        elif char in [">", ']', '}', ')']:
            if (x := queue.get()) != matches[char]:
                score += scores[char]
                break
        else:
            raise ValueError
    else:
        ac_score = 0
        while not queue.empty():
            char = queue.get()
            ac_score *= 5
            ac_score += ac_scores[r_matches[char]]
        autocomplete_scores.append(ac_score)

autocomplete_scores.sort()

print("Part 1: ", score)
print("Part 2: ", autocomplete_scores[len(autocomplete_scores)//2])
