# https://adventofcode.com/2024/day/19
import os

type StripesT = dict[str, list[str]]
type DataT = list[str]

type Stripes2T = dict[str, dict[str, dict[str, list[str]]]]

def read_input(filename: str) -> (StripesT, DataT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    stripes = {}
    data = []
    for s in raw_lines[0].rstrip().split(', '):
        key = s[0]
        if key in stripes.keys():
            stripes[key].append(s)
        else:
            stripes[key] = [s]

    for key in stripes.keys():
        stripes[key].sort(key=lambda x: len(x), reverse=True)

    for i in range(2, len(raw_lines)):
        data.append(raw_lines[i].rstrip())

    return (stripes, data)

def read_input_2(filename: str) -> (StripesT, DataT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    stripes = {}
    data = []
    for s in raw_lines[0].rstrip().split(', '):
        if len(s) == 1:
            key = s[0]
            if key not in stripes.keys():
                stripes[key] = {'1': {
                    '1': [s]
                }}
        elif len(s) == 2:
            key1 = s[0]
            key2 = s[1]
            if key1 in stripes.keys():
                if key2 not in stripes[key1].keys():
                    stripes[key1][key2] = {'1': [s]}
            else:
                stripes[key1] = {key2: {'1': [s]}}
        else:
            key1 = s[0]
            key2 = s[1]
            key3 = s[2]
            if key1 in stripes.keys():
                if key2 in stripes[key1].keys():
                    if key3 not in stripes[key1][key2].keys():
                        stripes[key1][key2][key3] = [s]
                else:
                    stripes[key1][key2] = {key3: [s]}
            else:
                stripes[key1] = {key2: {key3: [s]}}

    for key1 in stripes.keys():
        for key2 in stripes[key1].keys():
            for key3 in stripes[key1][key2].keys():
                stripes[key1][key2][key3].sort(key=lambda x: len(x), reverse=True)

    for i in range(2, len(raw_lines)):
        data.append(raw_lines[i].rstrip())

    return (stripes, data)


def check_rule(rule: str, stripes: StripesT) -> bool:
    if len(rule) == 0:
        return True
    char = rule[0]
    if char not in stripes.keys():
        return False
    flag = False
    for stripe in stripes[char]:
        if len(rule) >= len(stripe) and stripe == rule[:len(stripe)]:
            flag = check_rule( rule[len(stripe):], stripes)
            if flag:
                break
    return flag

def check_rule_count(rule: str, count: int, stripes: StripesT) -> int:
    if len(rule) == 0:
        return count + 1

    if len(rule) >= 3:
        char1 = rule[0]
        char2 = rule[1]
        char3 = rule[2]
        if char1 in stripes.keys() and char2 in stripes[char1].keys() and char3 in stripes[char1][char2]:
            for stripe in stripes[char1][char2][char3]:
                if len(rule) >= len(stripe) and stripe == rule[:len(stripe)]:
                    count = check_rule_count( rule[len(stripe):],count, stripes)
    elif len(rule) >= 2:
        char1 = rule[0]
        char2 = rule[1]
        if char1 in stripes.keys() and char2 in stripes[char1].keys() and '1' in stripes[char1][char2]:
            for stripe in stripes[char1][char2]['1']:
                if len(rule) >= len(stripe) and stripe == rule[:len(stripe)]:
                    count = check_rule_count( rule[len(stripe):], count, stripes)
    elif len(rule) >= 1:
        char1 = rule[0]
        if char1 in stripes.keys() and '1' in stripes[char1].keys() and '1' in stripes[char1]['1']:
            for stripe in stripes[char1]['1']['1']:
                if len(rule) >= len(stripe) and stripe == rule[:len(stripe)]:
                    count = check_rule_count( rule[len(stripe):], count, stripes)

    return count


def solution_part1(filename: str) -> int:
    stripes, data = read_input(filename)

    result = 0

    for item in data:
        if check_rule(item, stripes):
            result += 1


    return result

def solution_part2(filename: str) -> int:
    stripes, data = read_input_2(filename)

    result = 0
    for item in data:
        result += check_rule_count(item, 0,  stripes)

    return result

# assert (solution_part1('data/input_test_1.txt') == 6)
# print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_1.txt') == 16)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
