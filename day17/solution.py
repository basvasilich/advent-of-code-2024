# https://adventofcode.com/2024/day/17
import os

type CommandsT = list[str]
type DataT = list[list[str]]


def read_input(filename: str) -> (CommandsT, int, int, int):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return [[]]

    result = []
    A = 0
    B = 0
    C = 0
    for i in range(len(raw_lines)):
        if i == 0:
            A = int(raw_lines[i].rstrip().replace('Register A: ', ''))
        elif i == 1:
            B = int(raw_lines[i].rstrip().replace('Register B: ', ''))
        elif i == 2:
            C = int(raw_lines[i].rstrip().replace('Register C: ', ''))
        elif i == 4:
            s = raw_lines[i].rstrip().replace('Program: ', '')
            result = [int(x) for x in s.split(',')]
    return result, A, B, C

def get_combo(op: int, A: int, B: int, C: int) -> int:
    if 0 <= op <= 3:
        return op
    if op == 4:
        return A
    if op == 5:
        return B
    if op == 6:
        return C
    if op == 7:
        raise Exception('Invalid operation')

def process(op1, op2, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    if op1 == 0:
        return adv(op2, A, B, C, pointer, out_str)
    if op1 == 1:
        return bxl(op2, A, B, C, pointer, out_str)
    if op1 == 2:
        return bst(op2, A, B, C, pointer, out_str)
    if op1 == 3:
        return jnz(op2, A, B, C, pointer, out_str)
    if op1 == 4:
        return bxc(op2, A, B, C, pointer, out_str)
    if op1 == 5:
        return out(op2, A, B, C, pointer, out_str)
    if op1 == 6:
        return bdv(op2, A, B, C, pointer, out_str)
    if op1 == 7:
        return cdv(op2, A, B, C, pointer, out_str)

def adv(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    combo = get_combo(op, A, B, C)
    A = int(A / (2 ** combo))
    return A, B, C, pointer, out_str

def bxl(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    B = B ^ op
    return A, B, C, pointer, out_str


def bst(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    combo = get_combo(op, A, B, C)
    B = combo % 8
    return A, B, C, pointer, out_str


def jnz(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    if A == 0:
        return A, B, C, pointer, out_str

    return A, B, C, op, out_str


def bxc(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    B = B ^ C
    return A, B, C, pointer, out_str


def out(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    combo = get_combo(op, A, B, C)
    return A, B, C, pointer, out_str + ',' + str(combo % 8) if out_str != '' else str(combo % 8)

def bdv(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    combo = get_combo(op, A, B, C)
    B = int(A / (2 ** combo))
    return A, B, C, pointer, out_str

def cdv(op, A, B, C, pointer, out_str) -> (int, int, int, int, str):
    combo = get_combo(op, A, B, C)
    C = int(A / (2 ** combo))
    return A, B, C, pointer, out_str

def run_program(program, A, B, C) -> str:
    result = ''
    pointer = 0
    while pointer < len(program) - 1:
        op1 = program[pointer]
        op2 = program[pointer + 1]
        A, B, C, new_pointer, result = process(op1, op2, A, B, C, pointer, result)
        if new_pointer == pointer:
            pointer += 2
        else:
            pointer = new_pointer

    return result

def solution_part1(filename: str) -> str:
    program, A, B, C = read_input(filename)

    return run_program(program, A, B, C)

def solution_part2(filename: str) -> int:
    program, _, _, _ = read_input(filename)

    result = 0
    while True:
        new_program = run_program(program, result, 0,0)

        if new_program == ','.join([str(x) for x in program]):
            break

        result += 1

    return result

assert (solution_part1('data/input_test_1.txt') == '4,6,3,5,6,3,5,2,1,0')
print('Result Part 1: ', solution_part1('data/input_1.txt'))
assert (solution_part2('data/input_test_2.txt') == 117440)
print('Result Part 2: ', solution_part2('data/input_1.txt'))
