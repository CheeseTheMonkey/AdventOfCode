
from aoc_common import prep_file_by_name


#data = prep_file_by_name("day01.testinput")
data = prep_file_by_name("day01.input")

data = [int(a) for a in data]

output_count = []

print(len([z for x, y in zip(data, data[1:]) if (z := (y - x)) > 0]))

three_sums = [sum(three) for three in zip(data, data[1:], data[2:])]

print(len([z for x, y in zip(three_sums, three_sums[1:]) if (z := (y - x)) > 0]))
