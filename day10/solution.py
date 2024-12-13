# https://adventofcode.com/2024/day/10
import os
from copy import deepcopy

type SeenTrails = set[((int, int), (int, int))]
type SeenTrailsV2 = set[str]
type Trail = list[(int, int)]

def read_input(filename: str) -> list[list[int]]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    for row, line in enumerate(raw_lines):
        nums = list(line.rstrip())
        result.append(list(map(int, nums)))

    return result


def go_trail(data: list[list[int]], pos: (int, int), seen: SeenTrails, start: (int, int)) -> SeenTrails:
    row, col = pos
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return seen

    cur_h = data[row][col]
    if cur_h == 9:
        seen.add((start, pos))
        return seen

    if row - 1 >= 0 and data[row - 1][col] - cur_h == 1:
        seen = go_trail(data, (row - 1, col), seen,  start)
    if row + 1 < len(data) and data[row + 1][col] - cur_h == 1:
        seen = go_trail(data, (row + 1, col), seen,  start)
    if col - 1 >= 0 and data[row][col - 1] - cur_h == 1:
        seen = go_trail(data, (row, col - 1), seen,  start)
    if col + 1 < len(data[0]) and data[row][col + 1] - cur_h == 1:
        seen = go_trail(data, (row, col + 1), seen,  start)

    return seen


def go_trail_v2(data: list[list[int]], pos: (int, int), seen: SeenTrailsV2, trail: Trail ) -> SeenTrailsV2:
    row, col = pos
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return seen

    cur_h = data[row][col]
    trail.append(pos)
    if cur_h == 9:
        seen.add(''.join([str(x[0]) + '|' + str(x[1]) + '#' for x in trail]))
        return seen

    if row - 1 >= 0 and data[row - 1][col] - cur_h == 1:
        seen = go_trail_v2(data, (row - 1, col), seen,  trail)
    if row + 1 < len(data) and data[row + 1][col] - cur_h == 1:
        seen = go_trail_v2(data, (row + 1, col), seen,  trail)
    if col - 1 >= 0 and data[row][col - 1] - cur_h == 1:
        seen = go_trail_v2(data, (row, col - 1), seen,  trail)
    if col + 1 < len(data[0]) and data[row][col + 1] - cur_h == 1:
        seen = go_trail_v2(data, (row, col + 1), seen,  trail)

    return seen


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    result = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 0:
                seen = go_trail(data, (row, col), set(), (row, col))
                result += len(seen)

    return result

def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == 0:
                seen = go_trail_v2(data, (row, col), set(), [(row, col)])
                result += len(seen)

    return result

assert (solution_part1('data/input_test_2.txt') == 1)
assert (solution_part1('data/input_test_1.txt') == 36)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_3.txt') == 81)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
