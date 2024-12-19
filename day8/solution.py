# https://adventofcode.com/2024/day/8
import os
from copy import deepcopy

type PointT = (int, int)
type MapShapeT = (int, int)
type AntennasT = dict[str, list[PointT]]


def read_input(filename: str) -> (AntennasT, MapShapeT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    antennas: AntennasT = {}
    for row in range(len(raw_lines)):
        for col in range(len(raw_lines[row].rstrip())):
            char = raw_lines[row][col]
            if char != '.':
                if char in antennas.keys():
                    antennas[char].append((row, col))
                else:
                    antennas[char] = [(row, col)]

    return antennas, (len(raw_lines), len(raw_lines[0].rstrip()))


def get_antinodes(ant1: PointT, ant2: PointT) -> (PointT, PointT):
    x1, y1 = ant1
    x2, y2 = ant2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 > x2 and y1 >= y2:
        return (x2 - dx, y2 - dy), (x1 + dx, y1 + dy)
    elif x1 <= x2 and y1 > y2:
        return (x1 - dx, y1 + dy), (x2 + dx, y2 - dy)
    elif x1 < x2 and y1 <= y2:
        return (x1 - dx, y1 - dy), (x2 + dx, y2 + dy)

    return (x1 + dx, y1 - dy), (x2 - dx, y2 + dy)

def get_antinodes_v2(ant1: PointT, ant2: PointT, l_h, l_w) -> set[PointT]:
    x1, y1 = ant1
    x2, y2 = ant2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    result = set()
    if x1 > x2 and y1 >= y2:
        for k in range(1, max(l_h, l_w) + 1):
            result.add((x2 - k * dx, y2 - k * dy))
            result.add((x1 + k * dx, y1 + k * dy))
    elif x1 <= x2 and y1 > y2:
        for k in range(1, max(l_h, l_w) + 1):
            result.add((x1 - k * dx, y1 + k * dy))
            result.add((x2 + k * dx, y2 - k * dy))
    elif x1 < x2 and y1 <= y2:
        for k in range(1, max(l_h, l_w) + 1):
            result.add((x1 - k * dx, y1 - k * dy))
            result.add((x2 + k * dx, y2 + k * dy))
    else:
        for k in range(1, max(l_h, l_w) + 1):
            result.add((x1 + k * dx, y1 - k * dy))
            result.add((x2 - k * dx, y2 + k * dy))
    return result

def print_data(antennas: AntennasT, nodes: list[PointT], l_h: int, l_w: int):
    result = ''
    for row in range(l_h):
        result += '\n'
        for col in range(l_w):
            if (row, col) in nodes:
                result += '#'
            else:
                for key in antennas.keys():
                    if (row, col) in antennas[key]:
                        result += key
                result += '.'

    print(result)


def solution_part1(filename: str) -> int:
    data, (l_h, l_w) = read_input(filename)

    result = set()

    for key in data.keys():
        for i in range(len(data[key])):
            for j in range(i + 1, len(data[key])):
                ant1 = data[key][i]
                ant2 = data[key][j]
                antinodes = get_antinodes(ant1, ant2)
                for antinode in antinodes:
                    x, y = antinode
                    if x >= 0 and x < l_h and y >= 0 and y < l_w:
                        result.add(antinode)
    print_data(data, list(result), l_h, l_w)
    return len(result)


def solution_part2(filename: str) -> int:
    data, (l_h, l_w) = read_input(filename)

    result = set()

    for key in data.keys():
        for i in range(len(data[key])):
            for j in range(i + 1, len(data[key])):
                ant1 = data[key][i]
                ant2 = data[key][j]
                result.add(ant1)
                result.add(ant2)
                antinodes = get_antinodes_v2(ant1, ant2, l_h, l_w)
                for antinode in antinodes:
                    x, y = antinode
                    if x >= 0 and x < l_h and y >= 0 and y < l_w:
                        result.add(antinode)
    print_data(data, list(result), l_h, l_w)
    return len(result)

assert (solution_part1('data/input_test_1.txt') == 14)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_1.txt') == 34)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
