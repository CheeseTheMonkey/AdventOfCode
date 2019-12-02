

get_fuel_from_weight = lambda x: (x // 3) - 2

def get_fuel(weight):
    fuel = 0
    remaining_weight = get_fuel_from_weight(weight)
    while remaining_weight >= 0:
        fuel += remaining_weight
        remaining_weight = get_fuel_from_weight(remaining_weight)

    return fuel

if __name__ == '__main__':
    print("Part One: ", sum(get_fuel_from_weight(int(x)) for x in open("day1.input").readlines()))

    print("Part Two: ", sum(get_fuel(int(x)) for x in open("day1.input").readlines()))
