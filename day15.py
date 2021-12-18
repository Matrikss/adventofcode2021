import math
import time

import numpy as np

MAX_INT = 9000
RANGE = 40


def get_min_distance(distances: np.matrix, points_to_consider: set) -> tuple:
    min_dist = math.inf
    min_pos = 0
    for point in points_to_consider:
        if distances[point] < min_dist:
            min_dist = distances[point]
            min_pos = point
    return min_pos


def dijkstra(mapa: np.matrix, source: tuple, target: tuple) -> int:
    dist = np.zeros(mapa.shape, int) + MAX_INT
    queue = set()

    for i in range(source[0], target[0] + 1):
        for j in range(source[1], target[1] + 1):
            if -RANGE < i - j < RANGE:
                queue.add((i, j))

    dist[source] = 0
    x_len = mapa.shape[1]
    y_len = mapa.shape[0]
    assert x_len == y_len

    while len(queue) > 0:
        y, x = get_min_distance(dist, queue)

        queue.remove((y, x))
        if (y, x) == target:
            return dist[y, x]

        adjacency = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
        valid_adjacency = [i for i in adjacency if 0 <= i[0] < y_len and 0 <= i[1] < x_len]
        for vizinho in valid_adjacency:
            if vizinho in queue:
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

    start = time.time()
    part1 = dijkstra(matrix, (0, 0), (y_len - 1, x_len - 1))
    duration = time.time() - start

    print(f'Part 1: {part1} {duration}')

    complete_map = np.zeros((y_len * 5, x_len * 5), int)

    for i in range(0, complete_map.shape[0]):
        for j in range(0, complete_map.shape[1]):
            value = matrix[i % x_len, j % x_len] + i // x_len + j // x_len
            if value > 9:
                value -= 9
            complete_map[i, j] = value

    start = time.time()
    part2 = dijkstra(complete_map, (0, 0), (y_len * 5 - 1, x_len * 5 - 1))
    duration = time.time() - start

    print(f'Part 2: {part2} {duration}')
