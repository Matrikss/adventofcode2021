import math
import re
import collections

with open('input/input14.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')
    template = raw_lines[0]
    insertions = dict()
    regexes = dict()
    for i in range(2, len(raw_lines)):
        rline = raw_lines[i]
        broken = rline.split()
        insertions[broken[0]] = broken[2]
        regexes[broken[0]] = re.compile(f'(?={broken[0]})')

    for _ in range(0, 10):
        finds = dict()
        for k, v in insertions.items():
            for fi in re.finditer(regexes[k], template):
                finds[fi.regs[0][0]] = v

        sorted_inserts = sorted(finds.keys())
        offset = 1
        for i in sorted_inserts:
            template = f'{template[:i + offset]}{finds[i]}{template[i + offset:]}'
            offset += 1

    letters = list(template)
    frequency = collections.Counter(letters)

    min_f = math.inf
    max_f = 0
    for k, v in frequency.items():
        min_f = min(min_f, v)
        max_f = max(max_f, v)

    print(f'Part 1: {max_f - min_f}')
    print(f'Part 2: {2}')
