# coding: utf-8
from itertools import cycle, accumulate


def fft(received, pattern=[0, 1, 0, -1]):
    ret = ""
    for i in range(len(received)):
        c = cycle((item for sublist in [[a]*(i+1) for a in pattern] for item in sublist))
        next(c)
        ret += str(sum((next(c)*int(j) for j in received)))[-1]
    return ret

if __name__ == '__main__':
    received = open("day16.input").read().strip()
    out = received[::]
    for _ in range(100):
        out = fft(out)

    print("Part 1:", out[:8])


    offset = received[:7]
    full_input = received*10000
    offset_input = [int(a) for a in full_input[int(offset):]]
    out = offset_input[::]
    for _ in range(100):
        out = [a%10 for a in accumulate(out[::-1])][::-1]

    print("Part 2:", ''.join(str(a) for a in out[:8]))
