# https://adventofcode.com/2024/day/2
import os


def check_nums(nums: list[str]) -> bool:
    if len(nums) == 0:
        return False

    d = 'up' if int(nums[1]) - int(nums[0]) > 0 else 'down'
    if len(nums) > 2:
        for i in range(1, len(nums)):
            if abs(int(nums[i]) - int(nums[i - 1])) < 1 or abs(int(nums[i]) - int(nums[i - 1])) > 3:
                return False

            if d == 'up':
                if int(nums[i]) - int(nums[i - 1]) < 0:
                    return False
            else:
                if int(nums[i]) - int(nums[i - 1]) > 0:
                    return False

    return True


def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    result = 0
    for line in raw_lines:
        nums = line.split(' ')
        flag = check_nums(nums)
        if flag:
            result += 1

    return result


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    result = 0
    for line in raw_lines:
        nums = line.split(' ')
        flag = check_nums(nums)

        if flag:
            result += 1
        else:
            for i in range(len(nums)):
                flag = check_nums(nums[:i] + nums[i + 1:])
                if flag:
                    result += 1
                    break
    return result

assert (solution_part1('data/input_test_1.txt') == 2)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_1.txt') == 4)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
