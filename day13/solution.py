# https://adventofcode.com/2024/day/13
import os
from copy import deepcopy

type ButtonT = (int, int)
type PrizeT = (int, int)
type MachineT = (ButtonT, ButtonT, PrizeT)

def read_input(filename: str) -> list[MachineT]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    for i in range(0, len(raw_lines), 4):
        x1_str, y1_str = raw_lines[i].rstrip().replace('Button A: ', '').split(', ')
        button1 = (int(x1_str.replace('X+', '')), int(y1_str.replace('Y+', '')))
        x2_str, y2_str = raw_lines[i + 1].rstrip().replace('Button B: ', '').split(', ')
        button2 = (int(x2_str.replace('X+', '')), int(y2_str.replace('Y+', '')))
        x3_str, y3_str = raw_lines[i + 2].rstrip().replace('Prize: ', '').split(', ')
        prize = (int(x3_str.replace('X=', '')), int(y3_str.replace('Y=', '')))
        result.append((button1, button2, prize))
    return result


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    result = 0

    for machine in data:
        button1, button2, prize = machine
        x1, y1 = button1
        x2, y2 = button2
        x3, y3 = prize
        a = (x3 * y2 - y3 * x2) / (x1 * y2 - y1 * x2)
        b = (x3 * y1 - y3 * x1) / (x2 * y1 - y2 * x1)
        if a.is_integer() and b.is_integer():
            result += int(a) * 3 + int(b) * 1
    return  result

def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0

    for machine in data:
        button1, button2, prize = machine
        x1, y1 = button1
        x2, y2 = button2
        x_3, y_3 = prize
        x3 = 10000000000000 + x_3
        y3 = 10000000000000 + y_3
        a = (x3 * y2 - y3 * x2) / (x1 * y2 - y1 * x2)
        b = (x3 * y1 - y3 * x1) / (x2 * y1 - y2 * x1)
        if a.is_integer() and b.is_integer():
            result += int(a) * 3 + int(b) * 1
    return  result

assert (solution_part1('data/input_test_1.txt') == 480)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
print('Result Part 2: ', solution_part2('data/input_1.txt'))
