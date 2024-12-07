from common import read_input


def parse_lines(lines: list[str]) -> list[tuple]:
    out = []
    for line in lines:
        result, operands = line.split(": ")
        result = int(result)
        operands = [int(operand) for operand in operands.split()]
        out.append((result, operands))
    return out


def can_make(result, operands, try_concat=False):
    if len(operands) == 1:
        return result == operands[0]
    
    last = operands[-1]

    # Check if it's possible to get the result be multiplying this value:
    if result % last == 0:
        can_mul = can_make(result // last, operands[:-1], try_concat)
    else:
        can_mul = False

    # for concatenation, we can use powers of 10 greater than out last number, as that's what the next to last number becomes
    # a || b == (a*power of 10 up from b) + b
    pow_of_10 = 10 ** len(str(last))
    if try_concat and (result - last) % pow_of_10 == 0:
        can_concat = can_make((result - last) // pow_of_10, operands[:-1], try_concat)
    else:
        can_concat = False
    
    can_add = can_make(result - last, operands[:-1], try_concat)
    return can_add or can_mul or can_concat

def p1(equations: list[tuple]):
    total = 0
    for result, operands in equations:
        if can_make(result, operands):
            total += result
    print(f"Part One: {total}")


def p2(equations: list[tuple]):
    total = 0
    for result, operands in equations:
        if can_make(result, operands, True):
            total += result
    print(f"Part Two: {total}")


def day7():
    equations = parse_lines(read_input(7))
    
    p1(equations)
    p2(equations)
   


if __name__ == "__main__":
    day7()