import math
import re
import collections


def hail_mary(pairs: str, count):
    if count == 10:
        return pairs
    ins = insertions[pairs]
    one = f'{pairs[0]}{ins}'
    two = f'{ins}{pairs[1]}'
    return hail_mary(one, count + 1) + hail_mary(two, count + 1)[1:]


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

    cache = dict()

    tst = hail_mary(template[0:2], 0)
    cache[template[0:2]] = tst[1:]
    for i in range(1, len(template) - 1):
        print(i)
        pair = template[i:i + 2]
        if pair in cache:
            tst += cache[pair]
            continue
        res = hail_mary(pair, 0)[1:]
        cache[pair] = res
        tst += res

    template = tst

    letters = list(template)
    frequency = collections.Counter(letters)

    min_f = math.inf
    max_f = 0
    for k, v in frequency.items():
        min_f = min(min_f, v)
        max_f = max(max_f, v)

    print(f'Part 1: {max_f - min_f}')
    print(f'Part 2: {2}')
