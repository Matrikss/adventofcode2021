NEW_TIMER = 8
RESET_TIMER = 6
SPAWN = 0

# input = [3, 4, 3, 1, 2]

input = [3, 3, 5, 1, 1, 3, 4, 2, 3, 4, 3, 1, 1, 3, 3, 1, 5, 4, 4, 1, 4, 1, 1, 1, 3, 3, 2, 3, 3, 4, 2, 5, 1, 4, 1, 2, 2, 4, 2, 5, 1, 2, 2, 1, 1, 1, 1, 4, 5, 4, 3, 1, 4, 4, 4, 5, 1, 1, 4, 3, 4, 2, 1, 1, 1, 1, 5, 2, 1, 4, 2, 4, 2, 5, 5, 5, 3,
         3, 5, 4, 5, 1, 1, 5, 5, 5, 2, 1, 3, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 5, 1, 2, 1, 2, 5, 5, 2, 1, 1, 4, 2, 1, 4, 2, 1, 1, 1, 4, 2, 5, 1, 5, 1, 1, 3, 1, 4, 3, 1, 3, 2, 1, 3, 1, 4, 1, 2, 1, 5, 1, 2, 1, 4, 4, 1, 3, 1, 1, 1, 1, 1, 5, 2, 1,
         5, 5, 5, 3, 3, 1, 2, 4, 3, 2, 2, 2, 2, 2, 4, 3, 4, 4, 4, 1, 2, 2, 3, 1, 1, 4, 1, 1, 1, 2, 1, 4, 2, 1, 2, 1, 1, 2, 1, 5, 1, 1, 3, 1, 4, 3, 2, 1, 1, 1, 5, 4, 1, 2, 5, 2, 2, 1, 1, 1, 1, 2, 3, 3, 2, 5, 1, 2, 1, 2, 3, 4, 3, 2, 1, 1, 2,
         4, 3, 3, 1, 1, 2, 5, 1, 3, 3, 4, 2, 3, 1, 2, 1, 4, 3, 2, 2, 1, 1, 2, 1, 4, 2, 4, 1, 4, 1, 4, 4, 1, 4, 4, 5, 4, 1, 1, 1, 3, 1, 1, 1, 4, 3, 5, 1, 1, 1, 3, 4, 1, 1, 4, 3, 1, 4, 1, 1, 5, 1, 2, 2, 5, 5, 2, 1, 5]

cache = {}


def calc_stage(stage, end, now):
    if (stage, now) in cache:
        return cache[(stage, now)]

    if now >= end:
        return 1

    if stage == SPAWN:
        cache[(NEW_TIMER, now + 1)] = calc_stage(NEW_TIMER, end, now + 1)
        cache[(RESET_TIMER, now + 1)] = calc_stage(RESET_TIMER, end, now + 1)
        return cache[(NEW_TIMER, now + 1)] + cache[(RESET_TIMER, now + 1)]
    else:
        cache[(stage - 1, now + 1)] = calc_stage(stage - 1, end, now + 1)
        return cache[(stage - 1, now + 1)]


total1 = 0
for i in input:
    if (i, 0) not in cache:
        cache[(i, 0)] = calc_stage(i, 80, 0)
    total1 += cache[(i, 0)]

cache = {}
total2 = 0
for i in input:
    if (i, 0) not in cache:
        cache[(i, 0)] = calc_stage(i, 256, 0)
    total2 += cache[(i, 0)]

print(f'Part 1: {total1}')
print(f'Part 2: {total2}')
