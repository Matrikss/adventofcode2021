MAX_INT = 999
import numpy as np


def dijkstra(mapa: np.matrix, source: tuple, target: tuple) -> int:
    dist = np.zeros(mapa.shape, int) + MAX_INT
    queue = np.zeros(mapa.shape, int) + 1

    dist[source] = 1  # because of the multiplications to find the minimum edge, zero x something is always zero
    x_len = mapa.shape[1]
    y_len = mapa.shape[0]
    assert x_len == y_len

    while len(np.where(queue > 0)[0]) > 0:
        u = np.argmin(np.multiply(dist, queue))
        x = u % x_len
        y = u // x_len
        # ind = np.unravel_index(u, dist.shape) # alternative

        queue[y, x] = MAX_INT
        if (y, x) == target:
            return dist[y, x]

        adjacency = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
        valid_adjacency = [i for i in adjacency if 0 <= i[0] < y_len and 0 <= i[1] < x_len]
        for vizinho in valid_adjacency:
            if 0 < queue[vizinho] < MAX_INT:
                alt = dist[y, x] + mapa[vizinho]
                if alt < dist[vizinho]:
                    dist[vizinho] = alt


with open('input/input15.txt') as f:
    read_data = f.read()

    lines = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        lines.append(list(rline))

    matrix = np.matrix(lines, int)

    x_len = matrix.shape[1]
    y_len = matrix.shape[0]

    part1 = dijkstra(matrix, (0, 0), (y_len - 1, x_len - 1))

    print(f'Part 1: {part1 - 1}')
    print(f'Part 2: {2}')
