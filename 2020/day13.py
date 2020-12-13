
from operator import mul
from itertools import count


def find_next_bus(arrival, buses):
    buses = [int(bus) for bus in buses.split(',') if bus is not "x"]
    nexts = sorted([ (bus - (arrival % bus), bus) for bus in buses])
    return nexts[0]


def factored_buses(buses):
    buses_with_pos = sorted([(int(bus), idx) for idx, bus in enumerate(buses.split(',')) if bus is not 'x'], reverse=True)
    start = 1
    interval = 1
    for bus, offset in buses_with_pos:
        start = next((x for x in count(start, interval) if not (x + offset) % bus))
        interval *= bus
    return start



with open("day13.input") as f:
    arrival, buses = f.read().splitlines()
    arrival = int(arrival)

print "Part 1: ", reduce(mul, find_next_bus(arrival, buses), 1)
print "Part 2: ", factored_buses(buses)
