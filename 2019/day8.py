
from collections import Counter


if __name__ == '__main__':
    layers = open("day8.input").read().strip()
    layers = [layers[x:x+150] for x in range(0, len(layers), 150)]

    count_layers = [Counter(a) for a in layers]
    count_layers = sorted(count_layers, key=lambda x: x['0'])
    print("Part 1:", count_layers[0]['1'] * count_layers[0]['2'])


    # be careful with references...
    image = [[' ']*25, [' ']*25, [' ']*25, [' ']*25, [' ']*25, [' ']*25]
    for layer in reversed(layers):
        rows = [layer[x: x+25] for x in range(0, len(layer), 25)]
        for i, row in enumerate(rows):
            for j, pixel in enumerate(row):
                if pixel == "2":
                    continue
                if pixel == "0":
                    image[i][j] = ' '
                if pixel == "1":
                    image[i][j] = '#'
    print('Part 2:')
    print('\n'.join([''.join(row) for row in image]))
