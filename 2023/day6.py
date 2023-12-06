
from common import read_input
from math import prod



def get_better_distances(time: int, distance: int) -> list[int]:
    results = []
    for i in range(time):
        travelled = i * (time - i)
        if travelled > distance:
            results.append(travelled)
    return results


def main():
    time, distance = read_input(6)
    time = [int(t) for t in time.split()[1:]]
    distance = [int(d) for d in distance.split()[1:]]

    print(f"Part One: {prod([len(get_better_distances(time[i], distance[i])) for i in range(len(time))])}")

    time, distance = read_input(6)
    time = int(''.join(t for t in time.split()[1:]))
    distance = int(''.join(d for d in distance.split()[1:]))
    
    print(f"Part Two: {len(get_better_distances(time, distance))}")

    



if __name__ == '__main__':
    main()