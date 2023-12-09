
from common import read_input
from itertools import cycle
import math
from time import sleep



def main():
    lr, _, *nodes = read_input(8)
    node_map = {}
    for node in nodes:
        root, leaves = node.split(" = ")
        leaves = leaves.strip("()").split(", ")
        node_map[root] = {
            "L": leaves[0],
            "R": leaves[1]
        }
    
    node = "AAA"
    route = cycle(lr)
    steps = 0
    while node != "ZZZ":
        node = node_map[node][next(route)]
        steps += 1
    
    print(f"Part One: {steps}")

    nodes = [node for node in node_map.keys() if node.endswith("A")]
    steps = []
    for node in nodes:
        node_steps = 0
        route = cycle(lr)
        while not node.endswith("Z"):
            node = node_map[node][next(route)]
            node_steps += 1
        steps.append(node_steps)
    
    print(f"Part Two: {math.lcm(*steps)}")
    gcd = math.gcd(node_steps)
    print(len(lr), gcd, gcd/len(lr))


if __name__ == '__main__':
    main()