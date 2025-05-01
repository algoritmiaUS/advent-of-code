
import sys


def get_part_number(line: str, pos: int):
    i = pos-1
    while i > -1 and line[i].isdigit():
        i -= 1

    j = pos+1
    while j < len(line) and line[j].isdigit():
        j += 1

    return int(line[i+1:j])


def get_symbols(line: str):
    symbols = set()
    for i, c in enumerate(line):
        if c in "#%-=@/*&+$":
            symbols.add(i)
    return symbols


INPUT_PATH = "day_3\input.txt"
if len(sys.argv) > 1:
    INPUT_PATH = sys.argv[1]

with open(INPUT_PATH) as f:
    data = f.readlines()

n = len(data[0])
empty_line = "." * n
data.insert(0, empty_line)
data.append(empty_line)

res = 0
for i, line in enumerate(data[1:-1], 1):
    symbols = get_symbols(line)

    for symbol in symbols:
        part_numbers = []

        if symbol > 0 and line[symbol-1].isdigit():
            part_numbers.append(get_part_number(line, symbol-1))

        if symbol < len(line) - 1 and line[symbol+1].isdigit():
            part_numbers.append(get_part_number(line, symbol+1))

        last_line = data[i-1]
        if last_line[symbol].isdigit():
            part_numbers.append(get_part_number(last_line, symbol))
        else:
            if symbol > 0 and last_line[symbol-1].isdigit():
                part_numbers.append(get_part_number(last_line, symbol-1))
            if symbol < len(line) - 1 and last_line[symbol+1].isdigit():
                part_numbers.append(get_part_number(last_line, symbol+1))

        next_line = data[i+1]
        if next_line[symbol].isdigit():
            part_numbers.append(get_part_number(next_line, symbol))
        else:
            if symbol > 0 and next_line[symbol-1].isdigit():
                part_numbers.append(get_part_number(next_line, symbol-1))
            if symbol < len(line) - 1 and next_line[symbol+1].isdigit():
                part_numbers.append(get_part_number(next_line, symbol+1))

        if len(part_numbers) == 2:
            # print(part_numbers)  # TEMP
            product = 1
            for part_number in part_numbers:
                product *= part_number
            res += product

print(res)
