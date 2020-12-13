

directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

headings = ['N', 'E', 'S', 'W']


def navigate(insts):
    x, y = 0, 0
    facing = 1
    for inst, mag in insts:
        if inst == 'R':
            facing = (facing + (mag/90)) % 4
        elif inst == 'L':
            facing = (facing - (mag/90)) % 4
        else:
            if inst == 'F':
                direction = directions[headings[facing]]
            elif inst in directions:
                direction = directions[inst]
            else:
                raise ValueError

            x += direction[0] * mag
            y += direction[1] * mag

    return x, y


def navigate_by_waypoint(insts):
    x, y = 0, 0
    w_x, w_y = 10, 1
    for inst, mag in insts:
        if inst == 'R':
            for _ in range(mag/90):
                w_x, w_y = w_y, -w_x
        elif inst == 'L':
            for _ in range(mag/90):
                w_x, w_y = -w_y, w_x
        elif inst in directions:
            direction = directions[inst]
            w_x += direction[0] * mag
            w_y += direction[1] * mag
        elif inst == 'F':
            x += w_x * mag
            y += w_y * mag
        else:
            raise ValueError

    return x, y


data = [(line[0], int(line[1:])) for line in open("day12.input").read().splitlines()]

print "Part 1: ", sum((abs(a) for a in navigate(data)))
print "Part 2: ", sum((abs(a) for a in navigate_by_waypoint(data)))
