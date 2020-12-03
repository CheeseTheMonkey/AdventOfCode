from itertools import combinations
from operator import mul

def find_product(numbers, result=2020, item_count=2, output_string="Part 1: "):
    for a in combinations(l, item_count):
        if sum(a) == result:
            print output_string, reduce(mul, a, 1)
            break

l = [int(l) for l in open("day01.input").read().splitlines()]

find_product(l)
find_product(l, item_count=3, output_string="Part 2: ")
