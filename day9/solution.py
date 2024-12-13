# https://adventofcode.com/2024/day/9
import os
from copy import deepcopy


def read_input(filename: str) -> (list[(int, list[int])]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return []

    result = [int(x) for x in list(raw_lines[0].rstrip())]
    return result


def decode(data: list[str]) -> list[int]:
    result = []
    num_index = 0
    for index, num in enumerate(data):

        if index % 2 == 0:
            while num > 0:
                result.append(num_index)
                num -= 1
            num_index += 1
        else:
            while num > 0:
                result.append(-1)
                num -= 1
    return result

def check_sum(data: list[int]) -> int:
    result = 0
    for index, num in enumerate(data):
        if num >= 0:
            result += num * index
        else:
            break
    return result


def compress(data: list[int]) -> list[int]:
    w_pointer = 0
    r_pointer = len(data) - 1

    while w_pointer < r_pointer:
        w_num = data[w_pointer]
        r_num = data[r_pointer]
        if w_num >= 0:
            w_pointer += 1
        if r_num < 0:
            r_pointer -= 1
        if w_num < 0 <= r_num:
            data[w_pointer] = r_num
            data[r_pointer] = w_num
            w_pointer += 1
            r_pointer -= 1
    return data

def compress_v2(data: list[int]) -> list[int]:
    w_pointer = 0
    r_pointer = len(data) - 1
    num = ''
    hole = ''
    while w_pointer < r_pointer:
        w_num = data[w_pointer]
        r_num = data[r_pointer]
        if w_num >= 0:
            w_pointer += 1
        if r_num < 0:
            num = ''
            r_pointer -= 1

        if r_num >= 0 and (r_num == int(num[-1]) or num == ''):
            num += str(r_num)
            r_pointer -= 1

        if r_num >= 0 and (r_num == int(num[-1]) or num == ''):
            num += str(r_num)
            r_pointer -= 1



    return data


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    buf = decode(data)
    buf_compressed = compress(buf)
    result = check_sum(buf_compressed)

    return result


assert (solution_part1('data/input_test_1.txt') == 1928)

print('Result Part 1: ', solution_part1('data/input_1.txt'))
# assert (solution_part2('data/input_test_1.txt') == 11387)
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
