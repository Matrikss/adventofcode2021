START = 'start'
END = 'end'


def find_paths(lines: dict, position, small_visits: set) -> int:
    if position == END:
        return 1
    if position.islower() and position in small_visits:
        return 0
    num_of_paths = 0
    for next in lines[position]:
        new = small_visits.copy()
        if position.islower():
            new.add(position)
        num_of_paths += find_paths(lines, next, new)
    return num_of_paths


with open('input/input12.txt') as f:
    read_data = f.read()

    connections = dict()

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

    paths = find_paths(connections, START, set())

    print(f'Part 1: {paths}')
    print(f'Part 2: {2}')
