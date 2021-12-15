import math

counters = dict()


def hail_mary(pairs: str, count):
    if count == 10:
        return
    next = insertions[pairs]
    counters[next[0][1]] += 1
    hail_mary(next[0], count + 1)
    hail_mary(next[1], count + 1)


with open('input/input14.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')
    template = raw_lines[0]
    insertions = dict()

    for i in range(2, len(raw_lines)):
        rline = raw_lines[i]
        broken = rline.split()
        insertions[broken[0]] = [f'{broken[0][0]}{broken[2]}', f'{broken[2]}{broken[0][1]}']
        if broken[0][0] not in counters:
            counters[broken[0][0]] = 0

    for l in list(template):
        counters[l] += 1

    for i in range(0, len(template) - 1):
        # print(i)
        pair = template[i:i + 2]
        hail_mary(pair, 0)

    min_f = math.inf
    max_f = 0
    for k, v in counters.items():
        min_f = min(min_f, v)
        max_f = max(max_f, v)

    print(f'Part 1: {max_f - min_f}')
    print(f'Part 2: {2}')
