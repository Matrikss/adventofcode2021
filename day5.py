from sympy import Point, Segment
import numpy as np


def draw_horizontal(seg, board):
    res = seg.args
    a = res[0]
    b = res[1]

    if a[0] > b[0]:
        c = a
        a = b
        b = c
    for i in range(a[0], b[0] + 1):
        board[a[1], i] += 1


def draw_vertical(seg, board):
    res = seg.args
    a = res[0]
    b = res[1]

    if a[1] > b[1]:
        c = a
        a = b
        b = c
    for i in range(a[1], b[1] + 1):
        board[i, a[0]] += 1


def draw_diagonal(seg, board):
    res = seg.args
    a = res[0]
    b = res[1]

    if a[0] < b[0]:
        i = 1
        length = b[0] - a[0]
    else:
        i = -1
        length = a[0] - b[0]
    if a[1] < b[1]:
        j = 1
    else:
        j = -1

    x = a[0]
    y = a[1]
    board[y, x] += 1
    for w in range(0, length):
        x += i
        y += j
        board[y, x] += 1


with open('input/input5.txt') as f:
    read_data = f.read()

    horizontal_lines = []
    vertical_lines = []
    diagonal_lines = []

    max_x = 0
    max_y = 0
    raw_lines = read_data.split('\n')
    for rlines in raw_lines:
        line = rlines.split()
        begin = line[0]
        end = line[2]
        begin_coord = begin.split(',')
        end_coord = end.split(',')
        begin_point = Point(int(begin_coord[0]), int(begin_coord[1]))
        end_point = Point(int(end_coord[0]), int(end_coord[1]))

        max_x = max(max_x, int(begin_coord[0]))
        max_x = max(max_x, int(end_coord[0]))

        max_y = max(max_y, int(begin_coord[1]))
        max_y = max(max_y, int(end_coord[1]))

        if begin_point.coordinates[0] == end_point.coordinates[0]:
            vertical_lines.append(Segment(begin_point, end_point))
        elif begin_point.coordinates[1] == end_point.coordinates[1]:
            horizontal_lines.append((Segment(begin_point, end_point)))
        else:
            diagonal_lines.append((Segment(begin_point, end_point)))

    board1 = np.zeros((max_y + 1, max_x + 1), int)
    board2 = np.zeros((max_y + 1, max_x + 1), int)

    for h in horizontal_lines:
        draw_horizontal(h, board1)
        draw_horizontal(h, board2)

    for v in vertical_lines:
        draw_vertical(v, board1)
        draw_vertical(v, board2)

    for d in diagonal_lines:
        draw_diagonal(d, board2)

    print(f'Part 1: {len(np.where(board1 > 1)[0])}')
    print(f'Part 2: {len(np.where(board2 > 1)[0])}')
