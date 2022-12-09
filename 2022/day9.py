
movements = [line.split(' ') for line in open("day9.input").read().splitlines()]
#movements = [line.split(' ') for line in """R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2""".splitlines()]
#movements = [line.split(' ') for line in """R 5
#U 8
#L 8
#D 3
#R 17
#D 10
#L 25
#U 20""".splitlines()]

DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

class CoOrd(tuple):
    def __add__(self, value):
        return CoOrd(a + b for a, b in zip(self, value))


def move(count, rope, movement, visited):
    for _ in range(count):
        rope[0] += movement
        for i in range(len(rope) - 1):
            if rope[i][0] - rope[i+1][0] > 1:
                if rope[i][1] - rope[i+1][1] > 0:
                    rope[i+1] += (1, 1)
                elif rope[i+1][1] - rope[i][1] > 0:
                    rope[i+1] += (1, -1)
                else:
                    rope[i+1] += (1, 0)
            elif rope[i+1][0] - rope[i][0] > 1:
                if rope[i][1] - rope[i+1][1] > 0:
                    rope[i+1] += (-1, 1)
                elif rope[i+1][1] - rope[i][1] > 0:
                    rope[i+1] += (-1, -1)
                else:
                    rope[i+1] += (-1, 0)
            elif rope[i][1] - rope[i+1][1] > 1:
                if rope[i][0] - rope[i+1][0] > 0:
                    rope[i+1] += (1, 1)
                elif rope[i+1][0] - rope[i][0] > 0:
                    rope[i+1] += (-1, 1)
                else:
                    rope[i+1] += (0, 1)
            elif rope[i+1][1] - rope[i][1] > 1:
                if rope[i][0] - rope[i+1][0] > 0:
                    rope[i+1] += (1, -1)
                elif rope[i+1][0] - rope[i][0] > 0:
                    rope[i+1] += (-1, -1)
                else:
                    rope[i+1] += (0, -1)
        visited.add(rope[-1])

    return rope, visited


rope = [CoOrd((0, 0)), CoOrd((0,0))]
visited = set()
visited.add(rope[-1])

for direction, count in movements:
    rope, visited = move(int(count), rope, DIRECTIONS[direction], visited)

print(f"Part 1: {len(visited)}")

rope = [CoOrd((0, 0)), CoOrd((0,0)), CoOrd((0, 0)), CoOrd((0,0)), CoOrd((0, 0)), CoOrd((0,0)), CoOrd((0, 0)), CoOrd((0,0)), CoOrd((0, 0)), CoOrd((0,0))] 
visited = set()
visited.add(rope[-1])

for direction, count in movements:
    rope, visited = move(int(count), rope, DIRECTIONS[direction], visited)

print(f"Part 2: {len(visited)}")
