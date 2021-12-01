def count_increases(list):
    increases = 0
    i = 0
    j = 1
    while j < len(list):
        if list[j] > list[i]:
            increases += 1
        i += 1
        j += 1
    return increases


with open('input1.txt') as f:
    read_data = f.read()

    depths = read_data.split('\n')
    depths = [int(i) for i in depths]

    print(f'Part 1: {count_increases(depths)}')

    window_size = 3
    window_sums = []
    for i in range(len(depths) - window_size + 1):
        window_sums.append(sum(depths[i: i + window_size]))

    print(f'Part 2: {count_increases(window_sums)}')
