

#f = open("day4.test", "r")
f = open("day4.input", "r")

part1 = 0
part2 = 0
for line in f:
    elf1, elf2 = [set(range(int(elf.split('-')[0]), int(elf.split('-')[1]) + 1 )) for elf in line.strip().split(",")]
    if elf1.issuperset(elf2) or elf1.issubset(elf2):
        part1 += 1
    if elf1 & elf2:
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
