

#f = open("day3.test", "r")
f = open("day3.input", "r")

def get_priority(ordinal):
    if ordinal > 96:
        return ordinal - 96
    return ordinal - 38


priorities = 0
group = []
group_priorities = 0
for line in f:
    line = line.strip()
    one = set(line[:len(line)//2])
    two = set(line[len(line)//2:])
    common = get_priority(ord(list(one.intersection(two))[0]))
    priorities += common
    group.append(set(line))
    if len(group) == 3:
        group_priorities += get_priority(ord(list(group[0].intersection(group[1]).intersection(group[2]))[0]))
        group = []



print(f"Part 1: {priorities}")
print(f"Part 2: {group_priorities}")
