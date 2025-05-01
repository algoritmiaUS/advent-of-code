
import sys


INPUT_PATH = "day_1\input.txt"
if len(sys.argv) > 1:
    INPUT_PATH = sys.argv[1]

with open(INPUT_PATH) as f:
    data = f.readlines()


res = 0
for line in data:
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in line[::-1]:
        if c.isdigit():
            last = c
            break
    num = int(first + last)
    res += num

print(res)
