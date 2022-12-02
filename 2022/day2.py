
#f = open("day2.test", "r")
f = open("day2.input", "r")

score = 0
outcome = 0

for line in f:
    elf, me = line.split()
    elf = ord(elf) - 64
    me = ord(me) - 87
    score += me
    if elf == me:
        score += 3
    elif me == (elf % 3) + 1:
        score += 6
    outcome += ((me -1) * 3) + (((elf + me) % 3) + 1)


print(f"Part 1: {score}")
print(f"Part 1: {outcome}")
