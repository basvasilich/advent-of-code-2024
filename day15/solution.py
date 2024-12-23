# https://adventofcode.com/2024/day/16
import os

type PointT = (int, int)
type DataT = list[list[str]]
type MovesT = list[str]

def read_input(filename: str) -> (DataT, MovesT, PointT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    data = []
    moves = []
    start = (0, 0)
    flag = False
    for i in range(len(raw_lines)):
        if flag:
            for move in list(raw_lines[i].rstrip()):
                moves.append(move)
        elif raw_lines[i] == '\n':
            flag = True
            continue
        else:
            line = raw_lines[i]
            data.append(list(line.rstrip()))
            for j in range(len(line)):
                if line[j] == '@':
                    start = (i, j)

    return data, moves, start

def read_input_v2(filename: str) -> (DataT, MovesT, PointT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    data = []
    moves = []
    start = (0, 0)
    flag = False
    for i in range(len(raw_lines)):
        if flag:
            for move in list(raw_lines[i].rstrip()):
                moves.append(move)
        elif raw_lines[i] == '\n':
            flag = True
            continue
        else:
            line = raw_lines[i].rstrip()
            result = ''
            for j in range(len(line.rstrip())):
                if line[j] == '@':
                    start = (i, j)
                    result += '@.'
                elif line[j] == '#':
                    result += '##'
                elif line[j] == '.':
                    result += '..'
                elif line[j] == 'O':
                    result += '[]'
            data.append(list(result))

    return data, moves, start

def print_data(data: DataT) -> None:
    result = ''
    for row in data:
        result += ''.join(row) + '\n'
    print(result)

def read_str(data: DataT, point: PointT, d: str, l: int | None = None  ) -> str:
    row, col = point
    s = ''
    if d == '^':
        for i in range(row, row - l if l else -1, -1):
            if data[i][col] == '#':
                break
            elif data[i][col] == '.':
                s += data[i][col]
                break
            else:
                s += data[i][col]
    elif d == 'v':
        for i in range(row, l if l else len(data)):
            if data[i][col] == '#':
                break
            elif data[i][col] == '.':
                s += data[i][col]
                break
            else:
                s += data[i][col]
    elif d == '<':
        for i in range(col, -1, -1):
            if data[row][i] == '#':
                break
            elif data[row][i] == '.':
                s += data[row][i]
                break
            else:
                s += data[row][i]
    elif d == '>':
        for i in range(col, len(data[0])):
            if data[row][i] == '#':
                break
            elif data[row][i] == '.':
                s += data[row][i]
                break
            else:
                s += data[row][i]

    return s

def write_str(data: DataT, point: PointT, d: str, s: str) -> PointT:
    row, col = point
    if s is None:
        return row, col

    str_list = list(s)
    pointer = 0

    while pointer < len(str_list):
        char = str_list[pointer]
        if char == '@':
            point =  row, col

        data[row][col] = char
        if d == '^':
            row -= 1
        elif d == 'v':
            row += 1
        elif d == '<':
            col -= 1
        elif d == '>':
            col += 1
        pointer += 1

    return point

def move_s(s: str) -> str | None:
    if s is None or '.' not in s:
        return s
    if len(s) == 1:
        return s
    return '.' + s[:len(s)-1]

def calc_result(data: DataT) -> int:
    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'O':
                result += 100 * row + col
    return result

def calc_result_v2(data: DataT) -> int:
    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '[':
                result += 100 * row + col
    return result

def solution_part1(filename: str) -> int:
    data, moves, start = read_input(filename)

    print_data(data)
    for move in moves:
        print_data(move)

        s = read_str(data, start, move)
        new_s = move_s(s)
        start = write_str(data, start, move, new_s)
        print_data(data)
        print('-----------------')

    return  calc_result(data)

def solution_part2(filename: str) -> int:
    data, moves, start = read_input_v2(filename)

    print_data(data)
    for move in moves:
        print_data(move)

        if move == '<' or move == '>':
            s = read_str(data, start, move)
            new_s = move_s(s)
            start = write_str(data, start, move, new_s)
        elif move == '^':
            s1 = read_str(data, start, move)
            if '[' in s1:
                s2 = read_str(data, (start[0],start[1] + 1), move, len(s1))
                if len(s2) < len(s1):
                    s1 = read_str(data, start, move, len(s2))

                new_s1 = move_s(s1)
                new_s2 = move_s(s2)
                start = write_str(data, start, move, new_s1)
                write_str(data, (start[0],start[1] + 1), move, new_s2)
            elif ']' in s1:
                s2 = read_str(data, (start[0],start[1] - 1), move, len(s1))
                if len(s2) < len(s1):
                    s1 = read_str(data, start, move, len(s2))

                new_s1 = move_s(s1)
                new_s2 = move_s(s2)
                start = write_str(data, start, move,     new_s1)
                write_str(data, (start[0],start[1] - 1), move, new_s2)
        print_data(data)
        print('-----------------')

    return  calc_result_v2(data)



assert (solution_part1('data/input_test_1.txt') == 2028)
assert (solution_part1('data/input_test_2.txt') == 10092)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# assert (solution_part2('data/input_test_2.txt') == 9021)
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
