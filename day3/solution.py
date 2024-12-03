# https://adventofcode.com/2024/day/3
import os
import re

def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()


    if len(raw_lines) == 0:
        return 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    result = 0
    for line in raw_lines:
        test_str = line
        matches = re.finditer(regex, test_str)

        for match in matches:
            str1, str2 = match.groups()
            result += int(str1) * int(str2)

    return result


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()


    if len(raw_lines) == 0:
        return 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    result = 0
    apply = True
    for line in raw_lines:
        test_str = line
        matches = re.finditer(regex, test_str)

        for match in matches:
            if match.group() == "don't()":
                apply = False
            elif match.group() == "do()":
                apply = True
            elif apply:
                str1, str2 = match.groups()
                result += int(str1) * int(str2)

    return result
assert (solution_part1('data/input_test_1.txt') == 161)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_2.txt') == 48)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
