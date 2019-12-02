

def run_opcodes(opcodes):
    for x in range(0, len(opcodes), 4):
        opcode = opcodes[x:x+4]
        if opcode[0] == 99:
            break
        elif opcode[0] == 1:
            opcodes[opcode[3]] = opcodes[opcode[1]] + opcodes[opcode[2]]
        elif opcode[0] == 2:
            opcodes[opcode[3]] = opcodes[opcode[1]] * opcodes[opcode[2]]
        else:
            raise ValueError("Error, unknown opcode {} in position {}".format(opcode[0], x))
    return opcodes[0]


def find_noun_verb(opcodes, result):
    for noun in range(100):
        for verb in range(100):
            codes = opcodes[:]
            codes[1] = noun
            codes[2] = verb
            if run_opcodes(codes) == result:
                break
        else:
            continue
        break
    return (100 * noun) + verb


if __name__ == '__main__':
    # Part 1
    opcodes = [int(x) for x in open('day2.input').read().strip().split(',')]

    codes = opcodes[:]
    codes[1] = 12
    codes[2] = 2

    print("Part 1: ", run_opcodes(codes))

    print("Part 2: ", find_noun_verb(opcodes, 19690720))
