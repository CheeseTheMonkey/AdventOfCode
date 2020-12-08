
from collections import OrderedDict

class BootCode(object):
    def __init__(self):
        self.lines_run = OrderedDict()
        self.accumulator= 0
        self.current_instruction = 0

    def run(self, code):
        while self.current_instruction not in self.lines_run:
            if self.current_instruction >= len(code):
                return True, self.accumulator

            method, value = code[self.current_instruction].split()
            value = int(value)
            self.lines_run[self.current_instruction] = (method, value)
            getattr(self, method)(value)
        else:
            # We've found a repeated code
            return False, self.accumulator

    def acc(self, value):
        self.accumulator += value
        self.current_instruction += 1

    def jmp(self, value):
        self.current_instruction += value

    def nop(self, _):
        self.current_instruction += 1
