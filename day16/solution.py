# https://adventofcode.com/2024/day/16
import os

type PointT = (int, int)
type DataT = list[list[str]]

def read_input(filename: str) -> (DataT, PointT, PointT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    e = tuple()
    s = tuple()
    for i in range(len(raw_lines)):
        line = raw_lines[i]
        result.append(list(line.rstrip()))
        for j in range(len(line)):
            if line[j] == 'E':
                e = (i, j)
            if line[j] == 'S':
                s = (i, j)

    return result, s, e

def print_data(data: DataT) -> None:
    result = ''
    for row in data:
        result += ' '.join([str(x) if x == '#' else str(x).zfill(6) for x in row]) + '\n'
    print(result)



def get(data: DataT, point: PointT) -> str | int:
    row, col = point
    return data[row][col]

def check_point(data: DataT, point: PointT) -> bool:
    return check_point_boundaries(data, point) and isinstance(get(data, point), int)

def check_point_boundaries(data: DataT, point: PointT) -> bool:
    row, col = point
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return False
    return True


def solution_part1(filename: str) -> int:
    data, s ,e = read_input(filename)
    h = [((s[0]-2, s[1]), 'u', 1002)]

    data[s[0]][s[1]] = 0
    data[s[0]-1][s[1]] = 1001

    while len(h) > 0:
        point, d, next_val = h.pop(0)
        if not check_point_boundaries(data, point):
            continue
        if get(data, point) == '#':
            continue
        if get(data, point) == 'E':
            data[point[0]][point[1]] = next_val
        elif get(data, point) == '.' or (get(data, point) > 0 and next_val < get(data, point)):
            data[point[0]][point[1]] = next_val
            print_data(data)
            if d == 'u':
                h.append(((point[0] - 1, point[1]), 'u', next_val + 1))
                h.append(((point[0], point[1] - 1), 'l', next_val + 1000))
                h.append(((point[0], point[1] + 1), 'r', next_val + 1000))
            if d == 'd':
                h.append(((point[0] + 1, point[1]), 'd', next_val + 1))
                h.append(((point[0], point[1] - 1), 'l', next_val + 1000))
                h.append(((point[0], point[1] + 1), 'r', next_val + 1000))
            if d == 'l':
                h.append(((point[0], point[1] - 1), 'l', next_val + 1))
                h.append(((point[0] - 1, point[1]), 'u', next_val + 1000))
                h.append(((point[0] + 1, point[1]), 'd', next_val + 1000))
            if d == 'r':
                h.append(((point[0], point[1] + 1), 'r', next_val + 1))
                h.append(((point[0] - 1, point[1]), 'u', next_val + 1000))
                h.append(((point[0] + 1, point[1]), 'd', next_val + 1000))

    return  get(data, e)

def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0
    return  result

assert (solution_part1('data/input_test_1.txt') == 11048)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
