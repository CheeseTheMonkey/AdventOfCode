


def run_opcodes(opcodes, input_var=None):
    def get_var(var, mode):
        if mode == "1":
            return var
        else:
            return opcodes[var]
    index = 0
    ret_value = None
    while opcodes[index] != 99:
        opcode = f"{opcodes[index]:05d}"
        modes = opcode[2::-1]
        opcode = opcode[-2:]
        if opcode == "01":
            opcodes[opcodes[index+3]] = get_var(opcodes[index+1], modes[0]) + get_var(opcodes[index+2], modes[1])
            index += 4
        elif opcode == "02":
            opcodes[opcodes[index+3]] = get_var(opcodes[index+1], modes[0]) * get_var(opcodes[index+2], modes[1])
            index += 4
        elif opcode == "03":
            if not input_var:
                raise ValueError("Opcode 3 requires an input")
            opcodes[opcodes[index+1]] = input_var
            index += 2
        elif opcode == "04":
            ret_value = opcodes[opcodes[index+1]]
            index += 2
        elif opcode == "99":
            break
        else:
            raise ValueError("Error, unknown opcode {} in position {}".format(opcodes[index], index))
    return ret_value


print("Part 1:", run_opcodes([int(a) for a in open("day5.input").read().strip().split(",")], 1))
