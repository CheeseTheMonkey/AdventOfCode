from operator import mul

tree_map = open("day03.input").read().splitlines()


def get_collisions(x=1, y=1):
    loc_x = 0
    loc_y = 0
    max_x = len(tree_map[0])

    tree_count = 0

    while loc_y < len(tree_map):
        if tree_map[loc_y][loc_x] == '#':
            tree_count += 1
        loc_y += y
        loc_x = (loc_x + x) % max_x

    return tree_count

print "Part 1: ", get_collisions(x=3)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
collisions = [get_collisions(*coords) for coords in slopes]


print "Part 2: ", reduce(mul, collisions, 1)
