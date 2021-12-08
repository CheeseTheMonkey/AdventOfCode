
from aoc_common import read_file_by_line

def sort_string(value):
    return "".join(sorted(value))



data = [a.split(' | ') for a in read_file_by_line("day08.testinput")]
#data = [a.split(' | ') for a in read_file_by_line("day08.input")]

print("Part 1: ", sum(len([a for a in code.split() if len(a) not in (5,6)]) for _, code in data))

p2 = 0
for obs, code in data:
    obs = [sort_string(a) for a in obs.split()]
    code = [sort_string(a) for a in code.split()]
    mapping = {
        1: next((x for x in obs if len(x) == 2)),
        4: next((x for x in obs if len(x) == 4)),
        7: next((x for x in obs if len(x) == 3)),
        8: next((x for x in obs if len(x) == 7)),
    }
    mapping[9] = next((x for x in obs if len(x) == 6 and all(y in x for y in mapping[4])))
    mapping[0] = next((x for x in obs if len(x) == 6 and x != mapping[9] and all(y in x for y in mapping[1])))
    mapping[6] = next((x for x in obs if len(x) == 6 and x != mapping[9] and x != mapping[0]))
    mapping[3] = next((x for x in obs if len(x) == 5 and all(y in x for y in mapping[1])))
    mapping[5] = next((x for x in obs if len(x) == 5 and x != mapping[3] and all(y in mapping[9] for y in x)))
    mapping[2] = next((x for x in obs if len(x) == 5 and x != mapping[3] and x != mapping[5]))

    r_mapping = {v: str(k) for k, v in mapping.items()}
    t_code = [r_mapping[a] for a in code]
    p2 += int("".join(t_code))

print("Part 2: ", p2)
