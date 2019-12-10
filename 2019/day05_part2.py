


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
            if input_var is None:
                raise ValueError("Opcode 3 requires an input")
            opcodes[opcodes[index+1]] = input_var
            index += 2
        elif opcode == "04":
            ret_value = get_var(opcodes[index+1], modes[0])
            index += 2
        elif opcode == "05":
            if get_var(opcodes[index+1], modes[0]):
                index = get_var(opcodes[index+2], modes[1])
            else:
                index += 3
        elif opcode == "06":
            if not get_var(opcodes[index+1], modes[0]):
                index = get_var(opcodes[index+2], modes[1])
            else:
                index += 3
        elif opcode == "07":
            if get_var(opcodes[index+1], modes[0]) < get_var(opcodes[index+2], modes[1]):
                opcodes[opcodes[index+3]] = 1
            else:
                opcodes[opcodes[index+3]] = 0
            index += 4
        elif opcode == "08":
            if get_var(opcodes[index+1], modes[0]) == get_var(opcodes[index+2], modes[1]):
                opcodes[opcodes[index+3]] = 1
            else:
                opcodes[opcodes[index+3]] = 0
            index += 4
        elif opcode == "99":
            break
        else:
            raise ValueError("Error, unknown opcode {} in position {}".format(opcodes[index], index))
    return ret_value


print("Part 2:", run_opcodes([int(a) for a in open("day5.input").read().strip().split(",")], 5))
