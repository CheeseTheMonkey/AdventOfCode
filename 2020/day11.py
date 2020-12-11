
from copy import deepcopy

def part_one(seat_map, i, j):
    coords = [(i-1, j-1), (i-1, j), (i-1, j+1),
               (i, j-1),         (i, j+1),
               (i+1, j-1), (i+1, j), (i+1, j+1)]

    seats = []
    for y, x in coords:
        try:
            if 0 <= y < len(seat_map) and 0 <= x < len(seat_map[y]):
                seats.append(seat_map[y][x])
        except IndexError:
            continue
    return seats

def part_two(seat_map, i, j):
    vectors = ((-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    seats = []
    for mov_y, mov_x in vectors:
        x, y = j + mov_x, i + mov_y
        while 0 <= x < len(seat_map[0]) and 0 <= y < len(seat_map):
            if seat_map[y][x] is not '.':
                seats.append(seat_map[y][x])
                break
            x += mov_x
            y += mov_y
    return seats


def apply_transform(seat_map, surrounding_seats=part_one, surrounding_count=4):
    previous_occupied = -1
    occupied = sum([len([char for char in line if char == '#']) for line in seat_map])
    while not occupied == previous_occupied:
        new_map = deepcopy(seat_map)
        for i in range(len(seat_map)):
            for j in range(len(seat_map[i])):
                if seat_map[i][j] == 'L':
                    if '#' not in surrounding_seats(seat_map, i, j):
                        new_map[i][j] = '#'
                if seat_map[i][j] == '#':
                    if len([seat for seat in surrounding_seats(seat_map, i, j) if seat == '#']) >= surrounding_count:
                        new_map[i][j] = 'L'

        previous_occupied = occupied
        occupied = sum([len([char for char in line if char == '#']) for line in new_map])
        seat_map = new_map
    return occupied


if __name__ == '__main__':
    data = [[char for char in line] for line in open("day11.input").read().splitlines()]

    print "Part 1: ", apply_transform(data)

    print "Part 2: ", apply_transform(data, part_two, 5)
