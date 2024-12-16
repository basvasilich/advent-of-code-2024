# https://adventofcode.com/2024/day/11
import os
from copy import deepcopy

def read_input(filename: str) -> list[str]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return []

    return list(raw_lines[0].rstrip().split(' '))


def make_blink(list_str: list[str]) -> list[str]:
    read_pointer = 0

    result = []
    while read_pointer < len(list_str):
        cur_item = list_str[read_pointer]

        if cur_item == '0':
            result.append('1')
        elif len(cur_item) % 2 == 0:
            result.append(cur_item[:len(cur_item) // 2].lstrip('0') if cur_item[:len(cur_item) // 2].lstrip('0') != '' else '0' )
            result.append(cur_item[len(cur_item) // 2:].lstrip('0') if cur_item[len(cur_item) // 2:].lstrip('0') != '' else '0')
        else:
            result.append(str(int(cur_item) * 2024))

        read_pointer += 1

    return result

def solution_part1(filename: str) -> int:
    data = read_input(filename)

    count = 25
    while count > 0:
        data = make_blink(data)
        count -= 1

    return len(data)

def count_num(num) -> int:
    data = [num]
    count = 75
    while count > 0:
        data = make_blink(data)
        count -= 1

    return len(data)


def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0
    h = count_num('0')

    return result

# assert (solution_part1('data/input_test_1.txt') == 55312)
# print('Result Part 1: ', solution_part1('data/input_1.txt'))
print('Result Part 2: ', solution_part2('data/input_1.txt'))
