

from common import read_input
from collections import OrderedDict


def hash(sequence: str) -> int:
    hash = 0
    for char in sequence:
        hash = ((hash + ord(char)) * 17) % 256
    return hash




def main():
    line = read_input(15)[0]
    instructions = [instruction for instruction in line.split(',')]
    print(f"Part One: {sum(hash(instruction) for instruction in instructions)}")

    boxes: OrderedDict[int, dict[str, int]] = OrderedDict()
    for instruction in instructions:
        if '=' in instruction:
            label, focal = instruction.split('=')
            hsh = hash(label)
            boxes.setdefault(hsh, {})[label] = int(focal)

        elif '-' in instruction:
            label = instruction.split('-')[0]
            hsh = hash(label)
            if hsh in boxes and label in boxes[hsh]:
                del boxes[hsh][label]
    
    total = 0
    for box, lenses in boxes.items():
        for i, focal in enumerate(lenses.values(), start=1):
            total += (box + 1) * i * focal
    
    print(f"Part Two: {total}")
    


if __name__ == '__main__':
    main()