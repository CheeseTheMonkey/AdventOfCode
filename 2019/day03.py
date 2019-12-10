


def get_coord_list(move_list):
    coords = []
    current = (0, 0)

    for move in move_list:
        if move.startswith('U'):
            coords.extend([(current[0], current[1] + 1 + y) for y in range(int(move[1:]))])
        if move.startswith('D'):
            coords.extend([(current[0], current[1] - 1 - y) for y in range(int(move[1:]))])
        if move.startswith('R'):
            coords.extend([(current[0] + 1 + x, current[1]) for x in range(int(move[1:]))])
        if move.startswith('L'):
            coords.extend([(current[0] - 1 - x, current[1]) for x in range(int(move[1:]))])

        current = coords[-1]

    return coords


if __name__ == '__main__':
    move_lists = [x.strip().split(',') for x in open('day3.input').readlines()]

    coord_list = []
    for move_list in move_lists:
        coord_list.append(get_coord_list(move_list))

    coords = set.intersection(*(set(item) for item in coord_list))

    print("Part 1:", min((abs(x)+abs(y) for x,y in coords)))

    distances = [{xy: distance for distance, xy in enumerate(x, 1) if xy in coords} for x in coord_list]

    print("Part 2:", min((sum((item[coord] for item in distances)) for coord in coords)))
