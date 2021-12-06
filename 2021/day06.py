
from aoc_common import read_file

#data = read_file("day06.testinput")
data = read_file("day06.input")

fish_counts = [data.count(str(a)) for a in range(9)]

for i in range(256):
    if i == 80:
        print("Part 1: ", sum(fish_counts))
    new = fish_counts.pop(0)
    fish_counts[6] = new + fish_counts[6]
    fish_counts.append(new)

print("Part 2: ", sum(fish_counts))
