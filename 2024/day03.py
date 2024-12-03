from common import read_input
import re
import sys


def sum_ops(memory: str) -> int:
    operations = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    return sum((int(a)*int(b)) for a, b in [op[4:-1].split(',') for op in operations])


def p1(memory: str):
    print(f"Part 1: {sum_ops(memory)}")


def p2(memory: str):
    if "-t" in sys.argv:
        memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    
    new_memory, *memory_to_parse = memory.split("don't()")
    for chunk in memory_to_parse:
        if "do()" in chunk:
            new_memory += "".join(chunk.split("do()")[1:])
    print(new_memory)
    print(f"Part 2: {sum_ops(new_memory)}")


def main():
    memory = "".join(read_input(3))
    p1(memory)
    p2(memory)


if __name__ == "__main__":
    main()