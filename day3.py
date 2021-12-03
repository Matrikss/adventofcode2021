def find_most(numbers, position, untie):
    numbers_count = len(numbers)
    most = numbers_count / 2
    ones = 0
    for number in numbers:
        ones += int(number[position])
    if ones > most:
        return 1
    if ones == most:
        return untie
    else:
        return 0


def find_least(numbers, position, untie):
    numbers_count = len(numbers)
    most = numbers_count / 2
    ones = 0
    for number in numbers:
        ones += int(number[position])
    if ones > most:
        return 0
    if ones == most:
        return untie
    else:
        return 1


def find_rating(numbers, wanted, index, function):
    if len(numbers) == 1:
        return numbers[0]
    most = function(numbers, index, wanted)
    filtered = [n for n in numbers if int(n[index]) == most]
    return find_rating(filtered, wanted, index + 1, function)


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

    oxygen = int(find_rating(numbers, 1, 0, find_most), 2)
    co2 = int(find_rating(numbers, 0, 0, find_least), 2)

    print(f'Part 1: {gamma} * {epsilon} = {gamma * epsilon}')
    print(f'Part 2: {oxygen} * {co2} = {oxygen * co2}')
