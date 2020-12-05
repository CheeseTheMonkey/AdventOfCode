

class Seat(object):
    MAP = {
        'F': '0',
        'L': '0',
        'B': '1',
        'R': '1'
    }
    def __init__(self, identifier):
        self.seat_ID = int(''.join([self.MAP[char] for char in identifier]), 2)
        self.row = int(''.join([self.MAP[char] for char in identifier[:7]]), 2)
        self.column = int(''.join([self.MAP[char] for char in identifier[7:]]), 2)

data = open("day05.input").read().splitlines()

seats = [Seat(line) for line in data]
seat_ids = [seat.seat_ID for seat in seats]
max_seat_num = max(seat_ids)
min_seat_num = min(seat_ids)

print "Part 1 ", max_seat_num

print "Part 2 ", [i for i in range(min_seat_num, max_seat_num) if i not in seat_ids]


