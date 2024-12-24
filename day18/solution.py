# https://adventofcode.com/2024/day/18
import os

type PointT = (int, int)
type BytesT = set[PointT]
type MapT = list[list[str]]

def read_input(filename: str, l:int = 1024) -> BytesT:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return set()

    result = set()

    for i in range(min(len(raw_lines), l)):
        line = raw_lines[i]
        result.add(tuple(line.rstrip().split(',')))


    return result

def read_line(filename: str, l:int = 1024) -> str:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    return raw_lines[l].rstrip()

def make_data(bytes: BytesT, h: int = 70, w: int = 70) -> MapT:
    result = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append('.')
        result.append(row)

    for point in bytes:
        col, row = point
        result[int(row)][int(col)] = '#'

    return result

def print_data(data: MapT) -> None:
    result = ''
    for row in data:
        result += ' '.join([x if x == '#' or x == '.' else 'o' for x in row]) + '\n'
    print(result)

def get_min_next_value(data: MapT, point: PointT) -> str:
    row, col = point
    result = []
    for point in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row, col)]:
        i, j = point
        if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
            continue
        if data[i][j] == '.' or data[i][j] == '#':
            continue
        if i == row and j == col:
            result.append(int(data[i][j]))
        else:
            result.append(int(data[i][j]) + 1)
    return  str(min(result))

def check_bounds(data: MapT, point: PointT) -> bool:
    row, col = point
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]) or get_value(data, point) == '#':
        return False
    return True

def get_value(data: MapT, point: PointT) -> str:
    row, col = point
    return data[row][col]

def process(bytes: BytesT, h = 71, w=71) -> int:
    data = make_data(bytes, h, w)
    q = [(0, 0)]
    data[0][0] = '0'
    while len(q) > 0:
        point = q.pop()
        row, col = point
        cur_value = int(data[row][col])
        if check_bounds(data, (row - 1, col)):
            if get_value(data, (row - 1, col)) == '.':
                data[row - 1][col] = str(cur_value + 1)
                q.append((row - 1, col))
            elif get_value(data, (row - 1, col)) != '.' and int(get_value(data, (row - 1, col))) > cur_value + 1:
                data[row - 1][col] = str(cur_value + 1)
                q.append((row - 1, col))

        if check_bounds(data, (row + 1, col)):
            if get_value(data, (row + 1, col)) == '.':
                data[row + 1][col] = str(cur_value + 1)
                q.append((row + 1, col))
            elif get_value(data, (row + 1, col)) != '.' and int(get_value(data, (row + 1, col))) > cur_value + 1:
                data[row + 1][col] = str(cur_value + 1)
                q.append((row + 1, col))
        if check_bounds(data, (row, col - 1)):
            if get_value(data, (row, col - 1)) == '.':
                data[row][col - 1] = str(cur_value + 1)
                q.append((row, col - 1))
            elif get_value(data, (row, col - 1)) != '.' and int(get_value(data, (row, col - 1))) > cur_value + 1:
                data[row][col - 1] = str(cur_value + 1)
                q.append((row, col - 1))
        if check_bounds(data, (row, col + 1)):
            if get_value(data, (row, col + 1)) == '.':
                data[row][col + 1] = str(cur_value + 1)
                q.append((row, col + 1))
            elif get_value(data, (row, col + 1)) != '.' and int(get_value(data, (row, col + 1))) > cur_value + 1:
                data[row][col + 1] = str(cur_value + 1)
                q.append((row, col + 1))

    # print_data(data)
    result = get_value(data, (int(h) - 1, int(w) - 1))
    return int( result if  result != '.' else '-1')

def solution_part1(filename: str, h = 71, w=71) -> int:
    bytes = read_input(filename)
    return process(bytes, h, w)

def solution_part2(filename: str, h = 71, w=71, l = 1024) -> (int, int):
    p_l = l
    p_r = 3450
    while p_l < p_r:
        p = (p_l + p_r) // 2
        b = read_input(filename, p)
        result = process(b, h, w)
        if result == -1:
            p_r = p
        else:
            p_l = p + 1

    s = read_line(filename, p_l-1)
    return s


# assert (solution_part1('data/input_test_1.txt', 7 ,7) == 22)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# assert (solution_part2('data/input_test_2.txt', 7 ,7, 12) == '6,1')
print('Result Part 2: ', solution_part2('data/input_1.txt'))