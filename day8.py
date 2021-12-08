SEPARATOR = '|'
EASY_DIGITS = [2, 3, 4, 7]
EASY_DIGITS_DICT = {2: '1',
                    3: '7',
                    4: '4',
                    7: '8'}


def process1(signals, segments):
    res = []
    for signal in signals:
        if len(signal) == 2:
            segments[3] = set(signal)
            segments[6] = set(signal)
        else:
            res.append(signal)
    return res


def process3(signals, segments):
    res = []
    for signal in signals:
        if len(signal) == 5:
            s = set(signal)
            if segments[3].issubset(s):
                # it is a 3
                segments[7] = s.difference(segments[3]).difference(segments[4]).difference(segments[1])
                segments[4] = s.intersection(segments[4])
                segments[2] = segments[2].difference(segments[4])
            else:
                res.append(signal)
        else:
            res.append(signal)
    return res


def process4(signals, segments):
    res = []
    for signal in signals:
        if len(signal) == 4:
            segments[2] = set(signal).difference(segments[3])
            segments[4] = segments[2].copy()
        else:
            res.append(signal)
    return res


def process6(signals, segments):
    res = []
    for signal in signals:
        if len(signal) == 6:
            s = set(signal)
            if not segments[3].issubset(s):
                # it is a 6
                segments[6] = s.intersection(segments[3])
                segments[3] = segments[3].difference(segments[6])
                segments[5] = s.difference(segments[1]).difference(segments[2]).difference(segments[4]).difference(segments[6]).difference(segments[7])
            else:
                res.append(signal)
        else:
            res.append(signal)
    return res


def process7(signals, segments):
    res = []
    for signal in signals:
        if len(signal) == 3:
            segments[1] = set(signal).difference(segments[3])
        else:
            res.append(signal)
    return res


def get_number(digits, segments):
    string_num = ''
    for digit in digits:
        if len(digit) in EASY_DIGITS_DICT:
            string_num += EASY_DIGITS_DICT[len(digit)]
        elif set(digit) == segments[1].union(segments[3]).union(segments[4]).union(segments[6]).union(segments[7]):
            string_num += '3'
        elif set(digit) == segments[1].union(segments[3]).union(segments[4]).union(segments[5]).union(segments[7]):
            string_num += '2'
        elif set(digit) == segments[1].union(segments[2]).union(segments[4]).union(segments[6]).union(segments[7]):
            string_num += '5'
        elif set(digit) == segments[1].union(segments[2]).union(segments[4]).union(segments[5]).union(segments[6]).union(segments[7]):
            string_num += '6'
        elif set(digit) == segments[1].union(segments[2]).union(segments[3]).union(segments[4]).union(segments[6]).union(segments[7]):
            string_num += '9'
        else:
            string_num += '0'
    return int(string_num)


with open('input/input8.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')

    easy_digits = 0
    solution2 = 0
    for line in raw_lines:
        separated = line.split(SEPARATOR)
        digits = separated[1].split()
        for digit in digits:
            if len(digit) in EASY_DIGITS:
                easy_digits += 1
        signals = separated[0].split()
        segments = {}
        unprocessed = process1(signals, segments)
        unprocessed = process7(unprocessed, segments)
        unprocessed = process4(unprocessed, segments)
        unprocessed = process3(unprocessed, segments)
        unprocessed = process6(unprocessed, segments)
        # segments decoded
        solution2 += get_number(digits, segments)

    print(f'Part 1: {easy_digits}')
    print(f'Part 2: {solution2}')
