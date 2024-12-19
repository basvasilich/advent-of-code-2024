# https://adventofcode.com/2024/day/13
import os

import numpy as np
from PIL import Image

type RobotT = (int, int,int, int)


def print_data(data: list[RobotT], bounds: (int, int), name: str) -> None:
    tall, wide = bounds
    result = []
    for i in range(tall):
        d = []
        for j in range(wide):
            flag = False
            for k in range(len(data)):
                x, y, _, _ = data[k]
                if x == j and y == i:
                    flag = True
                    break
            if flag:
                d.append(255)
            else:
                d.append(0)
        result.append(d)
    img = Image.fromarray(np.array(result, dtype=np.uint8), 'L')

    # Сохраняем изображение
    img.save(f"img/{name}.png")

def read_input(filename: str) -> list[RobotT]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return []


    result = []
    for line in raw_lines:
        p, v = line.rstrip().split(' ')
        p_x, p_y = p.replace('p=', '').split(',')
        v_x, v_y = v.replace('v=', '').split(',')

        result.append((int(p_x), int(p_y), int(v_x), int(v_y)))

    return result

def solution_part1(filename: str, bounds: (int, int), seconds: int = 100) -> int:
    data = read_input(filename)
    tall, wide = bounds

    result = [0,0,0,0]

    j = 0
    while j < seconds:
        for i in range(len(data)):
            x, y, vx, vy = data[i]
            x += vx
            if x < 0:
                x = wide - abs(x) % wide
            elif x >= wide:
                x = x % wide
            y += vy
            if y < 0:
                y = tall - abs(y) % tall
            elif y >= tall:
                y = y % tall
            data[i] = (x, y, vx, vy)
        if (j - 92) % 101 == 0:
            print_data(data, bounds, f'frame_{j+1}')
        j += 1

    for i in range(len(data)):
        x, y, _, _ = data[i]
        if x < wide // 2 and y < tall // 2:
            result[0] += 1
        elif x > wide // 2 and y < tall // 2:
            result[1] += 1
        elif x < wide // 2 and y > tall // 2:
            result[2] += 1
        elif x > wide // 2 and y > tall // 2:
            result[3] += 1



    return  result[0]*result[1]*result[2]*result[3]


# assert (solution_part1('data/input_test_2.txt', (7, 11), 5) == 0)
# assert (solution_part1('data/input_test_1.txt', (7, 11)) == 12)
print('Result Part 1: ', solution_part1('data/input_1.txt', (103, 101), 10000))
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
