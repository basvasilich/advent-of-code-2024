# https://adventofcode.com/2024/day/19
import os

type GraphT = dict[str, set[str]]

def read_input(filename: str) -> GraphT:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    if len(raw_lines) == 0:
        return {}

    g = {}
    for s in raw_lines:
        key1, key2 = s.rstrip().split('-')
        if key1 in g.keys():
            g[key1].add(key2)
        else:
            g[key1] = set([key2])
        if key2 in g.keys():
            g[key2].add(key1)
        else:
            g[key2] = set([key1])

    return g

def dfs(g: GraphT, start: str, visited: list[str]) -> list[str]:
    visited.append(start)
    for node in g[start]:
        if node not in visited and len(visited) < 3:
            dfs(g, node, visited)
        else:
            return visited

def solution_part1(filename: str) -> int:
    g = read_input(filename)

    result = set()
    for key1 in g.keys():

        pairs_no_same = [(a, b) for a in g[key1] for b in g[key1] if a != b]
        for pair in pairs_no_same:
            tmp = [key1]
            key2, key3 = pair
            if key3 in g.keys() and key2 in g[key3] and ('t' ==  key1[0] or 't' == key2[0] or 't' == key3[0]):
                tmp.append(key2)
                tmp.append(key3)
                tmp.sort()
                result.add(tuple(tmp))
    return len(result)


assert (solution_part1('data/input_test_1.txt') == 7)
print('Result Part 1: ', solution_part1('data/input_1.txt'))
# assert (solution_part2('data/input_test_1.txt') == 16)
# print('Result Part 2: ', solution_part2('data/input_1.txt'))
