# https://adventofcode.com/2024/day/12
import os
from copy import deepcopy

type MapT = list[list[str]]
type PointT = (int, int)
type SeenPointsT = set[(int, int)]
type RegionKeyT = str
type AreaT = int
type PerimetrT = int

def read_input(filename: str) -> MapT:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    for line in raw_lines:
        result.append(list(line.rstrip()))

    return result

def process_region(data: MapT, point: PointT, region_key: RegionKeyT, seen: SeenPointsT, cur_area: int, cur_perimetr: int) -> (SeenPointsT, AreaT, PerimetrT):
    row, col = point
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return seen, cur_area, cur_perimetr

    if point in seen:
        return seen, cur_area, cur_perimetr

    if data[row][col] != region_key:
        return seen, cur_area, cur_perimetr

    seen.add(point)
    cur_area += 1

    if row - 1 < 0 or data[row-1][col] != region_key :
        cur_perimetr += 1
    if row + 1 == len(data) or data[row+1][col] != region_key :
        cur_perimetr += 1
    if col - 1 < 0 or data[row][col-1] != region_key:
        cur_perimetr += 1
    if col + 1 == len(data[0]) or data[row][col+1] != region_key:
        cur_perimetr += 1

    seen, cur_area, cur_perimetr = process_region(data, (row - 1, col), region_key, seen, cur_area, cur_perimetr)
    seen, cur_area, cur_perimetr = process_region(data, (row + 1, col), region_key, seen, cur_area, cur_perimetr)
    seen, cur_area, cur_perimetr = process_region(data, (row, col - 1), region_key, seen, cur_area, cur_perimetr)
    seen, cur_area, cur_perimetr = process_region(data, (row, col + 1), region_key, seen, cur_area, cur_perimetr)

    return seen, cur_area, cur_perimetr


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    seen = set()
    budget = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            seen, area, perimetr = process_region(data, (row, col), data[row][col], seen, 0, 0)
            budget += area * perimetr
    return budget

assert (solution_part1('data/input_test_1.txt') == 1930)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
