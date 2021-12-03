with open('input3.txt') as f:
    read_data = f.read()

    numbers = read_data.split('\n')

    total_numbers = len(numbers)
    number_len = len(numbers[0])

    count_ones = [0] * number_len

    for number in numbers:
        for i in range(0, number_len):
            count_ones[i] += int(number[i])

    most = total_numbers / 2
    gamma = ''
    epsilon = ''
    for i in range(0, number_len):
        if count_ones[i] > most:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(f'Part 1: {gamma} * {epsilon} = {gamma * epsilon}')
    # print(f'Part 2: {horizontal_pos} * {depth_part2} = {horizontal_pos * depth_part2}')
