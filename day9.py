import math

import numpy as np

visited = set()


def get_basin(map, lowest):
    ix_len = map.shape[1]
    iy_len = map.shape[0]
    ix = lowest[1]
    iy = lowest[0]
    if map[lowest] == 9:
        return
    if (iy, ix) in visited:
        return
    iadjacency = [(iy, ix - 1), (iy, ix + 1), (iy - 1, ix), (iy + 1, ix)]
    ivalid_adjacency = [i for i in iadjacency if 0 <= i[0] < iy_len and 0 <= i[1] < ix_len]
    visited.add((iy, ix))
    for i in ivalid_adjacency:
        get_basin(map, i)
    return


with open('input/input9.txt') as f:
    read_data = f.read()

    lines = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        lines.append(list(rline))

    matrix = np.matrix(lines, int)

    risk_level = 0
    basin_sizes = []

    x_len = matrix.shape[1]
    y_len = matrix.shape[0]
    for x in range(0, x_len):
        for y in range(0, y_len):
            height = matrix[y, x]
            adjacency = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
            valid_adjacency = [i for i in adjacency if 0 <= i[0] < y_len and 0 <= i[1] < x_len]
            higher_adjacency = [i for i in valid_adjacency if matrix[i] > height]
            if len(valid_adjacency) == len(higher_adjacency):
                risk_level += height + 1
                get_basin(matrix, (y, x))
                basin_sizes.append(len(visited))
                visited = set()

    basin_sizes.sort(reverse=True)
    part2 = math.prod(basin_sizes[0:3])

    print(f'Part 1: {risk_level}')
    print(f'Part 2: {part2}')
