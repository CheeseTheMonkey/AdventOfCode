




commands = """noop
addx 3
addx -5"""
commands = open("day10.test").read()
commands = open("day10.input").read()


def get_command(commands):
    for command in commands.splitlines():
        yield command


cycle = 1
x = 1
to_execute = 0
signal = 0

commands = get_command(commands)
screen = ""
while True:
    if cycle%40 in range(x, x+3):
        screen += '#'
    else:
        screen += '.'
    if cycle in (20, 60, 100, 140, 180, 220):
        signal += cycle * x
    if to_execute:
        cycle += 1
        x += to_execute
        to_execute = 0
        continue
    try:
        command = next(commands)
    except StopIteration:
        screen = screen[:-1] # I don't like this but I can't get my brain around the logic to make this unnecessary
        break
    if command == "noop":
        cycle += 1
        continue
    if command.startswith("addx"):
        cycle += 1
        to_execute = int(command.split(" ")[1])
        continue

print(f"Part 1: {signal}")
for i in range(0, len(screen), 40):
    print(screen[i:i+40])
