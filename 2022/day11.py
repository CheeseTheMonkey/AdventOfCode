
from collections import OrderedDict
from copy import deepcopy
import ast, operator
from math import prod, lcm

binOps = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def arithmeticEval (s):
    node = ast.parse(s, mode='eval')

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return binOps[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise Exception('Unsupported type {}'.format(node))

    return _eval(node.body)


monkeys = OrderedDict()
#with open("day11.test") as f:
with open("day11.input") as f:
    for monkey in f.read().split('\n\n'):
        monkey = monkey.splitlines()
        d = {
            'items': [int(item) for item in monkey[1].split(': ')[1].split(', ')],
            'operation': ' '.join(monkey[2].split(' ')[-2:]),
            'test': {
                'divisible': int(monkey[3].split(' ')[-1]),
                'true': ' '.join(monkey[4].split(' ')[-2:]).capitalize(),
                'false': ' '.join(monkey[5].split(' ')[-2:]).capitalize()
            },
            'activity': 0
        }
        monkeys[monkey[0].strip(':\n')] = d



def operate(monkeys, loops, calmdown=True):
    low_cm = lcm(prod([monkey['test']['divisible'] for monkey in monkeys.values()]))
    for _ in range(loops):
        for idx, monkey in monkeys.items():
            while monkey['items']:
                item = monkey['items'].pop()
                operation = monkey['operation']
                Some nonsense here
                if "old" in operation:
                    operation = operation.replace("old", str(item))
                item = arithmeticEval(" ".join((str(item), operation)))
                if calmdown:
                    item = item // 3
                else:
                    item = item % low_cm
                if item % monkey['test']['divisible']:
                    monkeys[monkey['test']['false']]['items'].append(item)
                else:
                    monkeys[monkey['test']['true']]['items'].append(item)
                monkeys[idx]['activity'] += 1

    return monkeys

print(f"Part 1: {prod(sorted(monkey['activity'] for monkey in operate(deepcopy(monkeys), 20).values())[-2:])}")
print(f"Part 2: {prod(sorted(monkey['activity'] for monkey in operate(deepcopy(monkeys), 10000, False).values())[-2:])}")
