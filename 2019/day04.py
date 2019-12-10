# coding: utf-8


def check_double(number):
    text = str(number)
    return any((text[i] == text[i-1] for i in range(1, len(text))))

def check_increase(number):
    text = str(number)
    return all((text[i] >= text[i-1] for i in range(1, len(text))))

print("Part 1:", len([x for x in range(264793, 803935) if check_double(x) and check_increase(x)]))

def check_only_double(number):
    text = str(number)
    substrings = [['']]
    for i in text:
        if i == substrings[-1][0]:
            substrings[-1].append(i)
        else:
            substrings.append([i])
    return any((len(x) == 2 for x in substrings))

print("Part 2:", len([x for x in range(264793, 803935) if check_only_double(x) and check_increase(x)]))
