# https://adventofcode.com/2024/day/7
import os
from copy import deepcopy


def read_input(filename: str) -> (list[(int, list[int])]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    for row, line in enumerate(raw_lines):
        target, nums = list(line.rstrip().split(': '))
        result.append((int(target), list(map(int, nums.split(' ')))))

    return result


def check_target(cur_nums: list[int], pointer: int, cur_result: int, cur_target) -> bool:
    if len(cur_nums) == 1:
        return cur_nums[0] == cur_target

    if cur_result > cur_target:
        return False

    if pointer == len(cur_nums) - 1:
        num = cur_nums[pointer]
        if cur_result + num == cur_target:
            return True

        if cur_result * num == cur_target:
            return True

        return False
    else:
        return (check_target(cur_nums, pointer + 1, cur_result + cur_nums[pointer], cur_target)
                or check_target(cur_nums,pointer + 1, cur_result * cur_nums[pointer], cur_target))


def check_target_v2(cur_nums: list[int], pointer: int, cur_result: int, cur_target) -> bool:
    if len(cur_nums) == 1:
        return cur_nums[0] == cur_target

    if cur_result > cur_target:
        return False
    num = cur_nums[pointer]
    if pointer == len(cur_nums) - 1:

        if cur_result + num == cur_target:
            return True

        if cur_result * num == cur_target:
            return True

        if int(str(cur_result) + str(num)) == cur_target:
            return True

        return False
    else:
        return (check_target_v2(cur_nums, pointer + 1, cur_result + cur_nums[pointer], cur_target)
                or check_target_v2(cur_nums, pointer + 1, cur_result * cur_nums[pointer], cur_target)
                or check_target_v2(cur_nums, pointer + 1, int(str(cur_result) + str(num)), cur_target))


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    result = 0

    for target, nums in data:
        if check_target(nums, 1, nums[0], target):
            result += target

    return result


def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0

    next_data = []
    for target, nums in data:
        if check_target(nums, 1, nums[0], target):
            result += target
        else:
            next_data.append((target, nums))

    for target, nums in next_data:
        if check_target_v2(nums, 1, nums[0], target):
            result += target

    return result


assert (solution_part2('data/input_test_2.txt') == 7290)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
# assert (solution_part1('data/input_test_1.txt') == 3749)
# print('Result Part 1: ', solution_part1('data/input_1.txt'))
# assert (solution_part2('data/input_test_1.txt') == 11387)
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
