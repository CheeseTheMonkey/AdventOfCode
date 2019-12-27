from collections import defaultdict
from queue import Queue
from math import ceil


def build_ingredient(string):
    y, x = string.split()
    return {'item': x, 'amount': int(y)}

def build_recipes(data):
    recipes = {}
    for equation in data:
        reactants, result = equation.split(' => ')
        result = build_ingredient(result)
        recipes[result['item']] = {
            'output': result['amount'],
            'ingredients': [build_ingredient(reactant) for reactant in reactants.split(', ')]
        }
    return recipes

def make_fuel(recipes, amount):
    supply = defaultdict(int)
    orders = Queue()
    orders.put({'item': 'FUEL', 'amount': int(amount)})
    ore_required = 0

    while not orders.empty():
        order = orders.get()
        if order['item'] == 'ORE':
            ore_required += order['amount']
        elif order['amount'] <= supply[order['item']]:
            supply[order['item']] -= order['amount']
        else:
            amount_needed = order['amount'] - supply[order['item']]
            recipe = recipes[order['item']]
            batches = ceil(amount_needed / recipe['output'])
            for ingredient in recipe['ingredients']:
                orders.put({'item': ingredient['item'], 'amount': ingredient['amount'] * batches})
            supply[order['item']] = batches * recipe['output'] - amount_needed

    return ore_required


if __name__ == '__main__':
    # Testing
    data = [
        "10 ORE => 10 A",
        "1 ORE => 1 B",
        "7 A, 1 B => 1 C",
        "7 A, 1 C => 1 D",
        "7 A, 1 D => 1 E",
        "7 A, 1 E => 1 FUEL",
    ]
    recipes = build_recipes(data)
    assert(make_fuel(recipes, 1) == 31)

    data = [x.strip() for x in open("day14.input").readlines()]
    recipes = build_recipes(data)
    print("Part 1:", make_fuel(recipes, 1))

    available_ore = 1000000000000
    lower = 3200000
    upper = 3300000
    while lower + 1 != upper:
        guess = (lower + upper) // 2
        needed = make_fuel(recipes, guess)
        if needed > available_ore:
            upper = guess
        else:
            lower = guess

    print("Part 2:", lower)
