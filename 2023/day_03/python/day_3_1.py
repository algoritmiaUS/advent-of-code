
import sys


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


res = 0
last_symbols = set()
symbols = get_symbols(data[0])
for i, line in enumerate(data):
    if i == len(data) - 1:
        next_symbols = set()
    else:
        next_symbols = get_symbols(data[i+1])

    i = 0
    while i < len(line):

        while i < len(line) and not line[i].isdigit():
            i += 1
        start = i
        # print(f"{start=}")  # TEMP
        
        if start == len(line):
            continue

        while i < len(line) and line[i].isdigit():
            i += 1
        if i == len(line):
            end = i + 1
        else:
            end = i

        is_part_number = (
            start - 1 in symbols
            or end in symbols
        )
        if not is_part_number:
            last_next_symbols = last_symbols | next_symbols
            for j in range(start-1, end+1):
                if j in last_next_symbols:
                    is_part_number = True
                    break
        
        if is_part_number:
            number = int(line[start:end])
            # print(f"{number=}, {start=}, {end=}")  # TEMP
            res += number
        
        i += 1
    
    last_symbols = symbols
    symbols = next_symbols

print(res)
