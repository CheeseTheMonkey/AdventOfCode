from collections import Counter


#in_cals = [l.strip() for l in open("day1.test").readlines()]
in_cals = [l.strip() for l in open("day1.input").readlines()]

elf_count = 1
elves = Counter()

for cals in in_cals:
    if not cals:
        elf_count += 1
        continue
    elves[elf_count] += int(cals)

print(f"Part 1: {max(elves.values())}")
print(f"Part 2: {sum((elf[1] for elf in elves.most_common()[:3]))}")
