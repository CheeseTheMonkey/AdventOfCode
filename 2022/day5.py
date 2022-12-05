
from collections import defaultdict
import copy


def get_crate_map(crate_input):
    crates = defaultdict(list)
    for line in crate_input[-2::-1]:
        for idx, char in enumerate(line[1::4], 1):
            if char != " ":
                crates[idx].append(char)

    return crates


def follow_instructions_cm9000(input_crates, instructions):
    crates = copy.deepcopy(input_crates)
    for instruction in instructions:
        _, count, _, source, _, dest = instruction.split()
        for _ in range(int(count)):
            crates[int(dest)].append(crates[int(source)].pop())
    return crates

def follow_instructions_cm9001(input_crates, instructions):
    crates = copy.deepcopy(input_crates)
    for instruction in instructions:
        _, count, _, source, _, dest = instruction.split()
        crates_to_move = crates[int(source)][-1 * int(count):]
        crates[int(source)] = crates[int(source)][:-1 * int(count)]
        crates[int(dest)].extend(crates_to_move)
    return crates


#with open("day5.test", "r") as f:
with open("day5.input", "r") as f:
    text = f.read()

crate_input, instructions = [t.split('\n') for t in text.split("\n\n")]

crates = get_crate_map(crate_input)

cm9000_crates = follow_instructions_cm9000(crates, [i for i in instructions if i])
cm9001_crates = follow_instructions_cm9001(crates, [i for i in instructions if i])

print(f'Part 1: {"".join(cm9000_crates[idx][-1] for idx in range(1, len(cm9000_crates) + 1))}')
print(f'Part 1: {"".join(cm9001_crates[idx][-1] for idx in range(1, len(cm9001_crates) + 1))}')
