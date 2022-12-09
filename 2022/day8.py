



def directions(i, j, imax, jmax):
    yield [(x, j) for x in range(i + 1, imax + 1)]
    yield [(x, j) for x in range(i - 1, -1, -1)]
    yield [(i, x) for x in range(j + 1, jmax + 1)]
    yield [(i, x) for x in range(j - 1, -1, -1)]



def process(i, j, trees, imax, jmax):
    height = trees[i,j]
    score = 1
    visible = False
    for line in directions(i, j, imax, jmax):
        distance = 0
        for location in line:
            distance += 1
            if trees[location] >= height:
                break
        else:
            visible = True
        score *= distance
    return visible, score

tree_map = {}
#input_str = open("day8.test").read()
input_str = open("day8.input").read()

for i, line in enumerate(input_str.splitlines()):
    for j, height in enumerate(line):
        tree_map[i, j] = int(height)

imax, jmax = i, j

results = [process(i, j, tree_map, imax, jmax) for (i, j) in tree_map]

print(f"Part 1: {sum(r[0] for r in results)}")
print(f"Part 2: {max(r[1] for r in results)}")
