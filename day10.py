import re

PATTERN_MINI_CHUNKS = re.compile('\\(\\)|\\[]|<>|{}')
PATTERN_OPEN_CHUNKS = re.compile('\\(|\\[|<|{')
PATTERN_CORRUPT_CHUNKS = re.compile('\\[[)>}]|\\([]>}]|<[)\\]}]|{[)>\\]]')

POINTS = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

PART2_POINTS = {'(': 1,
                '[': 2,
                '{': 3,
                '<': 4}


def get_points(line: str) -> tuple:
    groups = re.findall(PATTERN_MINI_CHUNKS, line)
    while len(groups) > 0:
        line = re.sub(PATTERN_MINI_CHUNKS, '', line)
        groups = re.findall(PATTERN_MINI_CHUNKS, line)
    opens = re.findall(PATTERN_OPEN_CHUNKS, line)
    if len(opens) == len(line):
        return 0, line
    corrupt = re.findall(PATTERN_CORRUPT_CHUNKS, line)
    if len(corrupt) > 0:
        return POINTS[corrupt[0][1]], 'dummy'
    raise Exception('not supposed!')


def get_points2(line: str) -> int:
    total = 0
    for letter in line:
        total = total * 5 + PART2_POINTS[letter]
    return total


with open('input/input10.txt') as f:
    read_data = f.read()

    part1_points = 0
    part2_points = []

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        points, line = get_points(rline)
        if points == 0:
            reversed_line = line[::-1]
            part2_points.append(get_points2(reversed_line))
        part1_points += points

    part2_points.sort()

    print(f'Part 1: {part1_points}')
    print(f'Part 2: {part2_points[len(part2_points) // 2]}')
