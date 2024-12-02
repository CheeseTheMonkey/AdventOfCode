from common import read_input
from copy import copy


def is_report_safe(report: list[int]) -> bool:
    if not (sorted(report) == report or sorted(report, reverse=True) == report):
        return False
    if not all((1<=abs(a-b)<=3 for a, b in zip(report, report[1:]))):
        return False
    return True


def p1(reports: list[list[int]]):
    safe = 0
    for report in reports:
        if not is_report_safe(report):
            continue
        safe += 1
    print(f"Part 1: {safe}")

def p2(reports: list[list[int]]):
    safe = 0
    for report in reports:
        report_safe = False
        for i in range(len(report)):
            copy_of_report = copy(report)
            del copy_of_report[i]
            if is_report_safe(copy_of_report):
                report_safe = True
                break
        if report_safe:
            safe += 1
    print(f"Part 2: {safe}")


        

def main():
    lines = read_input(2)
    lines = [[int(a) for a in line.split()] for line in lines]
    p1(lines)
    p2(lines)


if __name__ == "__main__":
    main()