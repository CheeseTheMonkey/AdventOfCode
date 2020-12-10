
from collections import Counter


data = sorted([int(i) for i in open("day10.input").read().splitlines()])

data = [0] + data + [data[-1] + 3]

joltage_differences = [b - a for a, b in zip(data, data[1:])]

c = Counter(joltage_differences)

print "Part 1: ", c[1] * c[3]

compatible = {}
for i, joltage in enumerate(data[:-1]):
    compatible[joltage] = [j for j in data[i+1:i+4] if j - joltage <=3]

permutations = {data[-1]: 1}
for joltage in data[-2::-1]:
    permutations[joltage] = sum(permutations[j] for j in compatible[joltage])

print "Part 2: ", permutations[0]
