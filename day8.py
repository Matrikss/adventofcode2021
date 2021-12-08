SEPARATOR = '|'
EASY_DIGITS = [2, 3, 4, 7]

with open('input/input8.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')

    easy_digits = 0
    for line in raw_lines:
        separated = line.split(SEPARATOR)
        digits = separated[1].split()
        for digit in digits:
            if len(digit) in EASY_DIGITS:
                easy_digits += 1

    print(f'Part 1: {easy_digits}')
    print(f'Part 2: {2}')
