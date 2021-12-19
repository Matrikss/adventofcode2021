import re

PATTERN_MINI_CHUNKS = re.compile('\\(\\)|\\[]|<>|{}')
PATTERN_OPEN_CHUNKS = re.compile('\\(|\\[|<|{')
PATTERN_CORRUPT_CHUNKS = re.compile('\\[[)>}]|\\([]>}]|<[)\\]}]|{[)>\\]]')

POINTS = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}


def get_points(line: str) -> int:
    groups = re.findall(PATTERN_MINI_CHUNKS, line)
    while len(groups) > 0:
        line = re.sub(PATTERN_MINI_CHUNKS, '', line)
        groups = re.findall(PATTERN_MINI_CHUNKS, line)
    opens = re.findall(PATTERN_OPEN_CHUNKS, line)
    if len(opens) == len(line):
        # TODO incomplete
        return 0
    corrupt = re.findall(PATTERN_CORRUPT_CHUNKS, line)
    if len(corrupt) > 0:
        return POINTS[corrupt[0][1]]
    raise Exception('not supposed!')


with open('input/input10.txt') as f:
    read_data = f.read()

    part1_points = 0

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        part1_points += get_points(rline)

    print(f'Part 1: {part1_points}')
    print(f'Part 2: {2}')
