# https://adventofcode.com/2024/day/4
import os


def read_input(filename: str) -> list[list[str]]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    for row, line in enumerate(raw_lines):
        result.append(list(line.rstrip()))
    return result


def search_xmas(data: list[list[str]], row: int, col: int) -> bool:
    if row < 1 or row >= len(data) - 1 or col < 1 or col >= len(data[0]) - 1:
        return False

    if data[row - 1][col - 1] == 'M' and data[row - 1][col + 1] == 'S' and data[row + 1][col - 1] == 'M' and data[row + 1][col + 1] == 'S':
        return True

    if data[row - 1][col - 1] == 'S' and data[row - 1][col + 1] == 'M' and data[row + 1][col - 1] == 'S' and data[row + 1][col + 1] == 'M':
        return True
    # https://adventofcode.com/2024/day/5
    import os

    def read_input(filename: str) -> (set[(str, str)], list[str]):
        with open(os.path.join(os.path.dirname(__file__), filename)) as file:
            raw_lines = file.readlines()
        if len(raw_lines) == 0:
            return set(), []

        rules = set()
        updates = []
        is_rules = True
        for row, line in enumerate(raw_lines):
            if line == '\n':
                is_rules = False
                continue
            if is_rules:
                rules.add(tuple(line.rstrip().split('|')))
            else:
                updates.append(line.rstrip().split(','))

        return rules, updates

    def check_updates(rules: set[(str, str)], update: list[str]) -> (int, (int, int)):
        flag = False
        wrong_pair = (0, 0)
        for i in range(1, len(update)):
            update_r = update[i]

            for j in range(i):
                update_l = update[j]
                if (update_r, update_l) in rules:
                    flag = True
                    wrong_pair = (i, j)
                    break
            if flag:
                break

        if not flag:
            return int(update[len(update) // 2]), wrong_pair

        return 0, wrong_pair

    def solution_part1(filename: str) -> int:
        rules, updates = read_input(filename)

        result = 0
        for update in updates:
            result += check_updates(rules, update)[0]

        return result

    def fix_update(rules: set[(str, str)], update: list[str]) -> list[str]:
        mid, pair = check_updates(rules, update)
        update[pair[0]], update[pair[1]] = update[pair[1]], update[pair[0]]
        mid, pair = check_updates(rules, update)
        if mid == 0:
            return fix_update(rules, update)
        else:
            return update

    def solution_part2(filename: str) -> int:
        rules, updates = read_input(filename)

        result = 0
        need_fix = []
        for update in updates:
            mid, pair = check_updates(rules, update)

            if mid == 0:
                need_fix.append(update)

        for update in need_fix:
            fixed_update = fix_update(rules, update)
            result += int(fixed_update[len(fixed_update) // 2])

        return result

    assert (solution_part1('data/input_test_1.txt') == 143)
    print('Result Part 1: ', solution_part1('data/input_1.txt'))
    assert (solution_part2('data/input_test_1.txt') == 123)
    print('Result Part 2: ', solution_part2('data/input_1.txt'))

    if data[row - 1][col - 1] == 'S' and data[row - 1][col + 1] == 'S' and data[row + 1][col - 1] == 'M' and data[row + 1][col + 1] == 'M':
        return True

    if data[row - 1][col - 1] == 'M' and data[row - 1][col + 1] == 'M' and data[row + 1][col - 1] == 'S' and data[row + 1][col + 1] == 'S':
        return True

    return False

def simple_search(data: list[list[str]], row: int, col: int, direction: str, word_val: str) -> bool:
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
        return False

    new_word_val = word_val + data[row][col]
    if new_word_val == 'XMAS':
        return True

    if len(new_word_val) == 4:
        return False

    if direction == 'up':
        return simple_search(data, row + 1, col, direction, new_word_val)
    elif direction == 'down':
        return simple_search(data, row - 1, col, direction, new_word_val)
    elif direction == 'left':
        return simple_search(data, row, col - 1, direction, new_word_val)
    elif direction == 'right':
        return simple_search(data, row, col + 1, direction, new_word_val)
    elif direction == 'up_left':
        return simple_search(data, row + 1, col - 1, direction, new_word_val)
    elif direction == 'up_right':
        return simple_search(data, row + 1, col + 1, direction, new_word_val)
    elif direction == 'down_left':
        return simple_search(data, row - 1, col - 1, direction, new_word_val)
    elif direction == 'down_right':
        return simple_search(data, row - 1, col + 1, direction, new_word_val)


def solution_part1(filename: str) -> int:
    data = read_input(filename)

    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'X':
                for d in ['up', 'down', 'left', 'right', 'up_left', 'up_right', 'down_left', 'down_right']:
                    if simple_search(data, row, col, d, ''):
                        result += 1
    return result



def solution_part2(filename: str) -> int:
    data = read_input(filename)

    result = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'A':
               if search_xmas(data, row, col):
                   result += 1
    return result

assert (solution_part1('data/input_test_2.txt') == 4)
assert (solution_part1('data/input_test_1.txt') == 18)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_3.txt') == 9)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
