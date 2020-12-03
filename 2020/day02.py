from collections import Counter

def get_password_tuple(line):
    bounds, letter, password = line.split()
    lower, upper = [int(a) for a in bounds.split('-')]
    letter = letter.strip(':')
    return (lower, upper, letter, password)


passwords = [get_password_tuple(l) for l in open("day02.input").read().splitlines()]
p1_valid_count = 0
p2_valid_count = 0

for lower, upper, letter, password in passwords:
    counts = Counter(password)
    if lower <= counts[letter] <= upper:
        p1_valid_count += 1
    if (password[lower - 1] == letter) ^ (password[upper - 1] == letter):
        p2_valid_count += 1

print "Part 1: ", p1_valid_count
print "Part 2: ", p2_valid_count

