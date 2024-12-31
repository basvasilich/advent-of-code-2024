# https://adventofcode.com/2024/day/21
import os
import re


def read_input(filename: str) -> [str]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return {}

    result = []
    for s in raw_lines:
        result.append(s.rstrip())

    return result

def mix(a: int, b: int) -> int:
    return a ^ b

def prune(a: int) -> int:
    return a % 16777216

def get_secret(num: int) -> int:
    a = prune(mix(num, num * 64))
    b = prune(mix(a, int(a / 32)))
    c = prune(mix(b, b * 2048))
    return c

def generate(num: int, n:int) -> int:
    while n > 0:
        num = get_secret(num)
        n -= 1
    return num

def solution_part1(filename: str) -> int:
    nums = read_input(filename)
    result = 0
    for num in nums:
        result += generate(int(num), 2000)


    return result

assert (solution_part1('data/input_test_1.txt') == 37327623)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
