
from aoc_common import read_file
from math import floor


def find_distance(data, pos):
    median = data[pos]
    return sum(abs(a - median) for a in data)

def triangle_number(n):
    return n * (n + 1) / 2

def find_distance_triangle_numbers(data):
    mean = sum(data) // len(data)
    return int(sum(triangle_number(abs(a - mean)) for a in data))


#data = sorted((int(a) for a in read_file("day07.testinput").split(',')))
data = sorted((int(a) for a in read_file("day07.input").split(',')))

median_pos = len(data)/2
if not isinstance(median_pos, int):
    min_distance = min(find_distance(data, floor(median_pos)), find_distance(data, floor(median_pos) + 1))
else:
    min_distance = find_distance(data, median_pos)

print("Part 1: ", min_distance)
print("Part 2: ", find_distance_triangle_numbers(data))
