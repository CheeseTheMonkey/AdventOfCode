

from aoc_common import read_file_by_line
from collections import Counter
from operator import itemgetter


def get_counts(data, index):
    count = Counter("")
    for y in range(len(data)):
        count.update(data[y][index])
    return sorted(count.items(), key=itemgetter(1))


#data = read_file_by_line("day03.testinput")
data = read_file_by_line("day03.input")

gamma = ""
epsilon = ""
oxygen = [line for line in data]
co2 = [line for line in data]

for x in range(len(data[1])):
    counts = get_counts(data, x)
    gamma = "{}{}".format(gamma, counts[1][0])
    epsilon = "{}{}".format(epsilon, counts[0][0])

    if not len(data) == len(oxygen):
        counts = get_counts(oxygen, x)

    if len(counts) == 1 or counts[0][1] == counts[1][1]:
        counts = [[], ["1",1]]
    oxygen = [a for a in oxygen if a[x] == counts[1][0]]

    if not len(data) == len(co2):
        counts = get_counts(co2, x)

    if len(counts) > 1 and counts[0][1] == counts[1][1]:
        counts = [["0",0]]
    co2 = [a for a in co2 if a[x] == counts[0][0]]

print(int(gamma, 2) * int(epsilon, 2))

print(int(oxygen[0], 2) * int(co2[0], 2))
