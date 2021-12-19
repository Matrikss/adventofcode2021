START = 'start'
END = 'end'


def find_paths(lines: dict, position, small_visits: set) -> int:
    if position == END:
        return 1
    if position in small_visits:
        return 0
    num_of_paths = 0
    for next in lines[position]:
        new = small_visits.copy()
        if position.islower():
            new.add(position)
        num_of_paths += find_paths(lines, next, new)
    return num_of_paths


ugly_practice = set()


def find_paths2(lines: dict, position, small_visits: set, path: list, exception: list):
    if position == END:
        path.append(END)
        ugly_practice.add(','.join(path))
        return
    if position in small_visits and position not in exception:
        return
    for next in lines[position]:
        new = small_visits.copy()
        if position.islower():
            if position in small_visits and position in exception:
                exception = list()
            new.add(position)
        path_copy = path.copy()
        path_copy.append(position)
        find_paths2(lines, next, new, path_copy, exception)
    return


with open('input/input12.txt') as f:
    read_data = f.read()

    connections = dict()
    small_caves = set()

    raw_lines = read_data.split('\n')
    for rline in raw_lines:
        line_split = rline.split('-')
        if line_split[0] in connections:
            connections[line_split[0]].append(line_split[1])
        else:
            connections[line_split[0]] = [line_split[1]]
        if line_split[1] in connections:
            connections[line_split[1]].append(line_split[0])
        else:
            connections[line_split[1]] = [line_split[0]]
        if line_split[0].islower():
            small_caves.add(line_split[0])
        if line_split[1].islower():
            small_caves.add(line_split[1])

    small_caves.remove(START)
    small_caves.remove(END)

    paths = find_paths(connections, START, set())
    for cave in small_caves:
        find_paths2(connections, START, set(), list(), [cave])

    print(f'Part 1: {paths}')
    print(f'Part 2: {len(ugly_practice)}')
