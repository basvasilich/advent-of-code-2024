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

numeric_keypad_map_short = {
    'A0': '<',
    'A1': '^<<',
    'A3': '^',
    'A4': '^^<<',
    'A9': '^^^',
    '01': '^<',
    '02': '^',
    '0A': '>',
    '14': '^',
    '17': '^^',
    '29': '>^^',
    '2A': 'v>',
    '37': '<<^^',
    '38': '<^^',
    '3A': 'v',
    '43': 'v>>',
    '45': '>',
    '48': '>^',
    '4A': '>>vv',
    '56': '>',
    '6A': 'vv',
    '74': 'v',
    '79': '>>',
    '80': 'vvv',
    '82': 'vv',
    '83': 'vv>',
    '97': '<<',
    '98': '<',
    '9A': 'vvv',
}

directional_keypad_map_l1 = {
    'A^': '<',
    'A>': 'v',
    'Av': '<v',
    'A<': 'v<<',
    '^v': 'v',
    '^>': 'v>',
    '^<': 'v<',
    '^A': '>',
    '>v': '<',
    '><': '<<',
    '>^': '<^',
    '>A': '^',
    '<v': '>',
    '<>': '>>',
    '<^': '>^',
    '<A': '>>^',
    'v^': '^',
    'v>': '>',
    'v<': '<',
    'vA': '>^',
}
pairs = set()

def convert_num_keys(num_keys: str, type: str = 'd') -> str:
    read_p = 1
    result = ''
    num_map = numeric_keypad_map_short
    if type == 'l1':
        num_map = directional_keypad_map_l1

    while read_p < len(num_keys):
        if num_keys[read_p - 1] ==  num_keys[read_p]:
            result += 'A'
        else:
            move = num_keys[read_p - 1] + num_keys[read_p]
            if move in num_map.keys():
                if type == 'n':
                    pairs.add(move)
                result += num_map[move] + 'A'
            else:
                print('!ERROR', move)
        read_p += 1
    return result

def extract_and_clean_number(s):
    cleaned = re.sub(r'\D', '', s)
    cleaned_number = cleaned.lstrip('0')
    return int(cleaned_number) if cleaned_number else 0


def convert_num_keys_all(num_keys: str, l: int = 2) -> str:
    k = convert_num_keys('A' + num_keys, 'n')
    while l> 0:
        k =  convert_num_keys('A' + k, 'l1')
        l -= 1
        print(l)
    return k

def solution_part1(filename: str) -> int:
    nums = read_input(filename)
    result = 0

    for num in nums:
        k = convert_num_keys_all(num)
        result += len(k) * extract_and_clean_number(num)

    return result

def solution_part2(filename: str) -> int:
    nums = read_input(filename)
    result = 0

    for num in nums:
        k = convert_num_keys_all(num, 25)
        result += len(k) * extract_and_clean_number(num)

    return result

assert (solution_part1('data/input_test_3.txt') == 68 * 29)
assert (solution_part1('data/input_test_2.txt') == 64 * 379)
assert (solution_part1('data/input_test_1.txt') == 126384)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
print('Result Part 2: ', solution_part2('data/input_1.txt'))
