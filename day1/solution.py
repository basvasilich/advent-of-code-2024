# https://adventofcode.com/2024/day/1
import collections
import os
from heapq import heappush, heappop

def solution_part1(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    left_heap = []
    right_heap = []
    result = 0
    for line in raw_lines:
        left, right = line.split('   ')
        left = int(left)
        right = int(right)
        heappush(left_heap, left)
        heappush(right_heap, right)

    while not len(left_heap) == 0:
        result += abs(heappop(left_heap) - heappop(right_heap))

    return result


def solution_part2(filename: str) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    left_heap = []
    right_heap = []
    result = 0
    for line in raw_lines:
        left, right = line.split('   ')
        left = int(left)
        right = int(right)
        heappush(left_heap, left)
        heappush(right_heap, right)

    list_of_letters = list(right_heap)
    letter_cnt = collections.Counter(list_of_letters)

    while not len(left_heap) == 0:
        left = heappop(left_heap)
        result += left * letter_cnt[left]

    return result

assert (solution_part1('data/input_test_1.txt') == 11)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_1.txt') == 31)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
