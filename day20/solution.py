# https://adventofcode.com/2024/day/20
import os

type PointT = (int, int)
type MapT = list[list[str]]


def read_input(filename: str) -> (MapT, PointT, PointT):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return []

    result = []

    start = (0, 0)
    end = (0, 0)

    for i in range(len(raw_lines)):
        line = raw_lines[i]
        a = list(line.rstrip())
        for j in range(len(a)):
            if a[j] == 'S':
                start = (i, j)
                a[j] = '.'
            if a[j] == 'E':
                end = (i, j)
                a[j] = '0'
        result.append(a)

    return result, start, end


def print_data(data: MapT) -> None:
    result = ''
    for row in data:
        result += ' '.join([x if x == '#' or x == '.' else 'o' for x in row]) + '\n'
    print(result)


def check_bounds(data: MapT, point: PointT) -> bool:
    row, col = point
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]) or get_value(data, point) == '#':
        return False
    return True


def get_value(data: MapT, point: PointT) -> str:
    row, col = point
    return data[row][col]


def process(i_data: MapT, start: PointT, end: PointT) -> MapT:
    data = [x.copy() for x in i_data]
    q = [end]
    data[end[0]][end[1]] = '0'
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
    return data

def remove_wall(i_data: MapT, point: PointT) -> MapT:
    row, col = point
    data = [x.copy() for x in i_data]
    data[row][col] = '.'
    return data

def find_walls(data: MapT) -> set[(int, PointT)]:
    result = set()
    for row in range(1, len(data)-1):
        for col in range(1, len(data[row])-1):
            if check_bounds(data, (row, col + 1)) and check_bounds(data, (row, col - 1)):
                if int(get_value(data, (row, col + 1))) >= 0 and int(get_value(data, (row, col - 1))) >= 0 and data[row][col] == '#':
                    result.add((abs(int(get_value(data, (row, col + 1))) - int(get_value(data, (row, col - 1))))-2, (row, col)))
            if check_bounds(data, (row + 1, col)) and check_bounds(data, (row - 1, col)):
                if int(get_value(data, (row + 1, col))) >= 0 and int(get_value(data, (row - 1, col))) >= 0 and data[row][col] == '#':
                    result.add((abs(int(get_value(data, (row + 1, col))) - int(get_value(data, (row - 1, col))))-2, (row, col)))
    return result


def solution_part1(filename: str) -> int:
    initial_map, start, end = read_input(filename)
    map = process(initial_map, start, end)
    walls = find_walls(map)
    result = 0

    h = {}
    for wall in walls:
        d,_ = wall
        if d >= 100:
            result += 1

    return result


# print('Result Part 1: ', solution_part1('data/input_test_1.txt'))
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
