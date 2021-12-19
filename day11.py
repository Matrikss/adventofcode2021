import numpy as np

with open('input/input11.txt') as f:
    read_data = f.read()

    lines = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        lines.append(list(rline))

    matrix = np.matrix(lines, int)

    x_len = matrix.shape[1]
    y_len = matrix.shape[0]

    total_flashes = 0
    step = 1
    while step <= 100:
        # print(step)
        matrix += 1
        flashed = set()
        flashers = np.where(matrix > 9)
        while len(flashed) != len(flashers[0]):
            for i in range(0, len(flashers[0])):
                x = flashers[1][i]
                y = flashers[0][i]
                if (y, x) in flashed:
                    continue
                adjacency = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x), (y + 1, x + 1), (y - 1, x - 1), (y + 1, x - 1), (y - 1, x + 1)]
                valid_adjacency = [i for i in adjacency if 0 <= i[0] < y_len and 0 <= i[1] < x_len]
                for adjacent in valid_adjacency:
                    matrix[adjacent] += 1
                flashed.add((y, x))
                total_flashes += 1
            flashers = np.where(matrix > 9)
        for flashed_octopus in flashed:
            matrix[flashed_octopus] = 0
        step += 1

    print(f'Part 1: {total_flashes}')
    print(f'Part 2: {2}')
