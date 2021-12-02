FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

with open('input2.txt') as f:
    read_data = f.read()

    instructions = read_data.split('\n')

    horizontal_pos = 0
    depth = 0
    depth_part2 = 0
    aim = 0

    for instruction in instructions:
        sections = instruction.split(' ')
        movement = sections[0]
        distance = int(sections[1])

        if movement == FORWARD:
            horizontal_pos += distance
            depth_part2 += aim * distance
            continue

        if movement == DOWN:
            depth += distance
            aim += distance
            continue

        if movement == UP:
            depth -= distance
            aim -= distance
            continue

    print(f'Part 1: {horizontal_pos} * {depth} = {horizontal_pos * depth}')
    print(f'Part 2: {horizontal_pos} * {depth_part2} = {horizontal_pos * depth_part2}')
