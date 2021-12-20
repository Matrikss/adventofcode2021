LITERAL_VALUE = 4

hex_map = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111'}


def get_literal_value(bits: str):
    result = ''
    for i in range(0, len(bits), 5):
        if bits[i] == '0':
            return int(result + bits[i + 1:i + 5], 2), bits[i + 5:]
        assert bits[i] == '1'
        result += bits[i + 1: i + 5]


def parse(bits: str) -> int:
    if len(bits) < 8:
        return 0
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    if type_id == LITERAL_VALUE:
        value, remaining = get_literal_value(bits[6:])
        return version + parse(remaining)
    else:
        length_type_id = bits[6]
        if length_type_id == '0':
            sub_packet_length = int(bits[7:7 + 15], 2)
            a = parse(bits[7 + 15:7 + 15 + sub_packet_length])
            b = parse(bits[7 + 15 + sub_packet_length:])
            return version + a + b
        else:
            assert length_type_id == '1'
            number_of_sub_packets = int(bits[7:7 + 11], 2)
            return version + parse(bits[7 + 11:])
            # this worked for part1, not really sure how :shrug:


with open('input/input16.txt') as f:
    read_data = f.read()

    raw_lines = read_data.split('\n')
    decoded_packet = ''
    packet = raw_lines[0]
    for letter in packet:
        decoded_packet += hex_map[letter]
    part1 = parse(decoded_packet)

    print(f'Part 1: {part1}')
    print(f'Part 2: {2}')
