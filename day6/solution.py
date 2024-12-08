# https://adventofcode.com/2024/day/6
import os
from copy import deepcopy


def read_input(filename: str) -> (dict[int, list[int]], dict[int, list[int]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    a_rows = {}
    a_cols = {}
    start = (0, 0)
    for row, line in enumerate(raw_lines):
        chars = list(line.rstrip())
        for col, char in enumerate(chars):
            if char == '^':
                start = (row, col)
            elif char == '#':
                if row in a_rows.keys():
                    a_rows[row].append(col)
                else:
                    a_rows[row] = [col]

                if col in a_cols.keys():
                    a_cols[col].append(row)
                else:
                    a_cols[col] = [row]
    for key in a_rows.keys():
        a_rows[key].sort()
    for key in a_cols.keys():
        a_cols[key].sort()

    return a_rows, a_cols, len(raw_lines), len(raw_lines[0]), start


def scan_up(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int)) -> (int, int):
    s_row, s_col = start
    if s_col not in a_cols.keys():
        return None

    obstacles = a_cols[s_col]
    for i in range(len(obstacles) - 1, -1, -1):
        obstacle = obstacles[i]

        if obstacle < s_row:
            return obstacle + 1, s_col
    return None

def scan_down(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int)) -> (int, int):
    s_row, s_col = start
    if s_col not in a_cols.keys():
        return None

    obstacles = a_cols[s_col]
    for i in range(len(obstacles)):
        obstacle = obstacles[i]
        if obstacle > s_row:
            return obstacle - 1, s_col
    return None

def scan_left(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int)) -> (int, int):
    s_row, s_col = start
    if s_row not in a_rows.keys():
        return None

    obstacles = a_rows[s_row]
    for i in range(len(obstacles) - 1, -1, -1):
        obstacle = obstacles[i]
        if obstacle < s_col:
            return s_row, obstacle + 1
    return None

def scan_right(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int)) -> (int, int):
    s_row, s_col = start
    if s_row not in a_rows.keys():
        return None

    obstacles = a_rows[s_row]
    for i in range(len(obstacles)):
        obstacle = obstacles[i]
        if obstacle > s_col:
            return s_row, obstacle - 1
    return None


def print_map(filename: str, seen: set[(int, int)]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    for row, line in enumerate(raw_lines):
        chars = list(line.rstrip())
        for s in seen:
            if s[0] == row:
                chars[s[1]] = 'X'
        print(''.join(chars) + '\n')
        print('\n-------------------\n')

def check_loop(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int), d: str,) -> bool:
    if d == 'up':
        s_up = scan_up(a_rows, a_cols, l_rows, l_cols, start)
        if s_up is None:
            return False
        s_right = scan_right(a_rows, a_cols, l_rows, l_cols, s_up)
        if s_right is None:
            return False
        s_down = scan_down(a_rows, a_cols, l_rows, l_cols, s_right)
        if s_down is not None and s_down[0] < start[0]:
            return False
        return True
    if d == 'down':
        s_down = scan_down(a_rows, a_cols, l_rows, l_cols, start)
        if s_down is None:
            return False
        s_left = scan_left(a_rows, a_cols, l_rows, l_cols, s_down)
        if s_left is None:
            return False
        s_up = scan_up(a_rows, a_cols, l_rows, l_cols, s_left)
        if s_up is not None and s_up[0] > start[0]:
            return False
        return True
    if d == 'left':
        s_left = scan_left(a_rows, a_cols, l_rows, l_cols, start)
        if s_left is None:
            return False
        s_up = scan_up(a_rows, a_cols, l_rows, l_cols, s_left)
        if s_up is None:
            return False
        s_right = scan_right(a_rows, a_cols, l_rows, l_cols, s_up)
        if s_right is not None and s_right[1] < start[1]:
            return False
        return True
    if d == 'right':
        s_right = scan_right(a_rows, a_cols, l_rows, l_cols, start)
        if s_right is None:
            return False
        s_down = scan_down(a_rows, a_cols, l_rows, l_cols, s_right)
        if s_down is None:
            return False
        s_left = scan_left(a_rows, a_cols, l_rows, l_cols, s_down)
        if s_left is not None and s_left[1] > start[1]:
            return False
        return True
    return False


def scan_ahead(a_rows: dict[int, list[int]], a_cols: dict[int, list[int]], l_rows, l_cols, start: (int, int), d: str,
               seen: set[(int, int)], filename: str, count, skip = False) -> (set[(int, int)], int):
    s_row, s_col = start

    if not skip and  check_loop(a_rows, a_cols, l_rows, l_cols, start, d):
        count += 1

    if d == 'up':
        s_next = scan_up(a_rows, a_cols, l_rows, l_cols, start)
        if s_next is None:
            for i in range(s_row -1, -1):

                seen.add((i, s_col))
            return seen, count

        for j in range(s_row, s_next[0] - 1, -1):
            seen.add((j, s_col))

        seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, s_next, 'right', seen, filename, count)
        return seen, count

    if d == 'down':
        s_next = scan_down(a_rows, a_cols, l_rows, l_cols, start)
        if s_next is None:
            for i in range(s_row, l_rows):
                seen.add((i, s_col))
            return seen, count

        for j in range(s_row, s_next[0] + 1):
            seen.add((j, s_col))

        seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, s_next, 'left', seen, filename, count)
        return seen, count

    if d == 'left':
        s_next = scan_left(a_rows, a_cols, l_rows, l_cols, start)
        if s_next is None:
            for i in range(s_col, -1, -1):
                seen.add((s_row, i))
            return seen, count

        for j in range(s_col, s_next[1] - 1, -1):
            seen.add((s_row, j))

        seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, s_next, 'up', seen, filename, count)
        return seen, count

    if d == 'right':
        s_next = scan_right(a_rows, a_cols, l_rows, l_cols, start)
        if s_next is None:
            for i in range(s_col, l_cols):
                seen.add((s_row, i))
            return seen, count

        for j in range(s_col, s_next[1] + 1):
            seen.add((s_row, j))

        seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, s_next, 'down', seen, filename, count)

        return seen, count


    return seen, count



def solution_part1(filename: str) -> int:
    a_rows, a_cols, l_rows, l_cols, start = read_input(filename)
    seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, start, 'up', {(start[0], start[1])}, filename, 0)

    return len(seen)


def solution_part2(filename: str) -> int:
    a_rows, a_cols, l_rows, l_cols, start = read_input(filename)
    seen, count = scan_ahead(a_rows, a_cols, l_rows, l_cols, start, 'up', {(start[0], start[1])}, filename, 0, skip = True)

    return count

assert (solution_part1('data/input_test_1.txt') == 41)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_1.txt') == 6)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
