import numpy as np

with open('input/input9.txt') as f:
    read_data = f.read()

    lines = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        lines.append(list(rline))

    matrix = np.matrix(lines, int)

    risk_level = 0

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

    print(f'Part 1: {risk_level}')
    print(f'Part 2: {2}')
