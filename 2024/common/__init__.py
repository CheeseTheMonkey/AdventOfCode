import argparse


def read_input(day: int):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store_true')
    args = parser.parse_args()
    filename = f'inputs/day{day:02d}.{"test_" if args.t else ""}input'
    return [line.strip() for line in open(filename).readlines()]
