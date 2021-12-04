import math

import numpy as np


def parse_bingo():
    boards = []
    with open('input/input4.txt') as f:
        read_data = f.read()
        lines = read_data.split('\n')

        numbers = lines.pop(0).split(',')
        lines.pop(0)

        current_board = []
        for line in lines:
            if line == '':
                matrix = np.matrix(current_board, dtype=int)
                boards.append(matrix)
                current_board = []
                continue
            current_board.append(line.split())
    return numbers, boards


def has_bingo(marks):
    rows = np.max(marks, axis=0)
    cols = np.max(marks, axis=1)

    min_row = np.min(rows)
    min_col = np.min(cols)

    return min_row == 0 or min_col == 0


def get_score(bingo_board, numbers):
    marks = (bingo_board * 0) + 1

    for n in numbers:
        res = np.where(bingo_board == int(n))
        if len(res[0]) == 0 or len(res[1]) == 0:
            continue
        marks[res[0][0], res[1][0]] = 0
        if has_bingo(marks):
            return np.sum(np.multiply(bingo_board, marks) * int(n)), numbers.index(n)

    raise Exception("Assumption FAIL!")


sequence, bingo_boards = parse_bingo()

final_score = 0
lose_score = 0
min_index = math.inf
max_index = 0
for board in bingo_boards:
    score, index = get_score(board, sequence)

    if index < min_index:
        min_index = index
        final_score = score

    if index > max_index:
        max_index = index
        lose_score = score

print(f'Part 1: {final_score}')
print(f'Part 2: {lose_score}')
