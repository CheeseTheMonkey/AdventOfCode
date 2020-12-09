
from itertools import combinations




def find_weakness(data):
    previous_numbers = []
    for number in data:
        if len(previous_numbers) < 25:
            previous_numbers.append(number)
            continue
        if number not in [sum(i) for i in combinations(previous_numbers, 2)]:
            return number
        del previous_numbers[0]
        previous_numbers.append(number)


def find_summed_numbers(data, target):
    for idx, number in enumerate(data):
        summed_numbers = [number]
        for j in range(idx + 1, len(data)):
            summed_numbers.append(data[j])
            if sum(summed_numbers) == target:
                return min(summed_numbers) + max(summed_numbers)
            if sum(summed_numbers) > target:
                break

if __name__ == '__main__':
    data = [int(line) for line in open("day09.input").read().splitlines()]
    weakness = find_weakness(data)
    print "Part 1: ", weakness
    print "Part 2: ", find_summed_numbers(data, weakness)
