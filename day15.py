import math

import numpy as np


def path_finder(mapa: np.matrix, pos: tuple, previous_pos: set, end_pos: tuple) -> int:
    if pos == end_pos:
        return mapa[pos]
    x_len = mapa.shape[1]
    y_len = mapa.shape[0]
    x = pos[1]
    y = pos[0]
    adjacency = [(y, x + 1), (y + 1, x)]
    valid_adjacency = [i for i in adjacency if i[0] < y_len and i[1] < x_len]
    not_visited = set(valid_adjacency).difference(previous_pos)

    if pos == (0, 0):
        this_risk = 0
    else:
        this_risk = mapa[pos]

    lowest = math.inf
    for prox in not_visited:
        cost = path_finder(mapa, prox, previous_pos.union({pos}), end_pos)
        lowest = min(cost, lowest)
    return this_risk + lowest


with open('input/input15.txt') as f:
    read_data = f.read()

    lines = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        lines.append(list(rline))

    matrix = np.matrix(lines, int)

    x_len = matrix.shape[1]
    y_len = matrix.shape[0]

    part1 = path_finder(matrix, (0, 0), set(), (y_len - 1, x_len - 1))

    print(f'Part 1: {part1}')
    print(f'Part 2: {2}')
