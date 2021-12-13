import numpy as np

TRANSLATE = {'x': 1,
             'y': 0}

with open('input/input13.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')
    max_x = 0
    max_y = 0
    dots = []
    # dots
    for i in range(0, len(raw_lines)):
        rline = raw_lines[i]
        if rline == "":
            i += 1
            break
        coords = rline.split(',')
        x = int(coords[0])
        y = int(coords[1])
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        dots.append((x, y))

    paper = np.zeros((max_y + 1, max_x + 1), int)
    for dot in dots:
        paper[dot[1], dot[0]] = 1

    part1 = 0
    # folds
    for j in range(i, len(raw_lines)):
        rline = raw_lines[j]
        words = rline.split()
        fold = words[2].split('=')
        axis = TRANSLATE[fold[0]]
        pos = int(fold[1])
        fold = np.flip(paper, axis)
        if axis == 0:
            folded = paper[:pos, :max_x + 1] + fold[:pos, :max_x + 1]
        else:
            folded = paper[:max_y + 1, :pos] + fold[:max_y + 1, :pos]
        if part1 == 0:
            part1 = len(np.where(folded > 0)[0])
        paper = folded

    print(f'Part 1: {part1}')
    print(f'Part 2: {paper}')  # BFKRCJZU (visually decoded)
