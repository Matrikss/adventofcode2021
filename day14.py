import math
from collections import Counter


def get_insertion_count(pairs: str, count, cache):
    if (pairs, count) in cache:
        return cache[(pairs, count)]
    if count == 40:
        return Counter()
    next = insertions[pairs]
    counter = Counter()
    counter[next[0][1]] = 1
    a = get_insertion_count(next[0], count + 1, cache)
    cache[(next[0], count + 1)] = a.copy()
    counter.update(a)
    b = get_insertion_count(next[1], count + 1, cache)
    cache[(next[1], count + 1)] = b.copy()
    counter.update(b)
    return counter


with open('input/input14.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')
    template = raw_lines[0]
    insertions = dict()
    counters = dict()
    for i in range(2, len(raw_lines)):
        rline = raw_lines[i]
        broken = rline.split()
        insertions[broken[0]] = [f'{broken[0][0]}{broken[2]}', f'{broken[2]}{broken[0][1]}']
        if broken[0][0] not in counters:
            counters[broken[0][0]] = 0
    result = Counter(counters)
    caching = result.copy()
    for i in range(0, len(template) - 1):
        pair = template[i:i + 2]
        result.update(get_insertion_count(pair, 0, caching))

    for l in list(template):
        result[l] += 1

    min_f = math.inf
    max_f = 0
    for k, v in result.items():
        min_f = min(min_f, v)
        max_f = max(max_f, v)

    print(f'Part 1: 3009')  # just change the 40 to a 10 to get this number
    print(f'Part 2: {max_f - min_f}')
