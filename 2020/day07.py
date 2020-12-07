import re


test = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

contains_re = re.compile(r"(\d+) (.*?) bag[,|s|.]*")


def parse_data(data):
    bag_map = {}

    for line in data:
        bag, contents = line.split(" bags contain")
        contains = contains_re.findall(contents)
        bag_map[bag] = {k:int(v) for v, k in contains}

    return bag_map


def bag_contains(bag_map, starting_bag, bag_to_find):
    if bag_to_find in bag_map[starting_bag]:
        return True
    return any([bag_contains(bag_map, bag, bag_to_find) for bag in bag_map[starting_bag]])

def bag_count(bag_map, starting_bag, top=False):
    if not bag_map[starting_bag]:
        return 1
    contains = sum([(v * bag_count(bag_map, k)) for k, v in bag_map[starting_bag].items()])
    if not top:
        contains += 1
    return contains

data = open("day07.input").read().splitlines()
bag_map = parse_data(data)


print "Part 1: ", len([bag for bag in bag_map if bag_contains(bag_map, bag, "shiny gold")])

assert(bag_count(parse_data(test.splitlines()), "shiny gold", top=True) == 126)

print "Part 2: ", bag_count(bag_map, "shiny gold", top=True)
