from collections import Counter



data = open("day06.input").read().splitlines()


counts = 0
questions = set()

for line in data:
    if not line:
        counts += len(questions)
        questions = set()
        continue
    for char in line:
        questions.add(char)

counts += len(questions)

print "Part 1: ", counts


counter = Counter()
people = 0
total = 0

for line in data:
    if not line:
        total += len([v for v in counter.values() if v == people])
        people = 0
        counter.clear()
        continue
    counter.update(line)
    people += 1

total += len([v for v in counter.values() if v == people])

print "Part 2: ", total
