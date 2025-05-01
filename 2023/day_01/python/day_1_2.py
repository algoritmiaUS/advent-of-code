
import sys


INPUT_PATH = "day_1\input.txt"
if len(sys.argv) > 1:
    INPUT_PATH = sys.argv[1]

with open(INPUT_PATH) as f:
    data = f.readlines()


res = 0
for line in data:

    used = ""
    for c in line:
        if c.isdigit():
            first = c
            break
        used += c
        if used.endswith("one"):
            first = "1"
            break
        elif used.endswith("two"):
            first = "2"
            break
        elif used.endswith("three"):
            first = "3"
            break
        elif used.endswith("four"):
            first = "4"
            break
        elif used.endswith("five"):
            first = "5"
            break
        elif used.endswith("six"):
            first = "6"
            break
        elif used.endswith("seven"):
            first = "7"
            break
        elif used.endswith("eight"):
            first = "8"
            break
        elif used.endswith("nine"):
            first = "9"
            break

    used = ""
    for c in line[::-1]:
        if c.isdigit():
            last = c
            break
        used = c + used
        if used.startswith("one"):
            last = "1"
            break
        elif used.startswith("two"):
            last = "2"
            break
        elif used.startswith("thre"):
            last = "3"
            break
        elif used.startswith("four"):
            last = "4"
            break
        elif used.startswith("five"):
            last = "5"
            break
        elif used.startswith("six"):
            last = "6"
            break
        elif used.startswith("seven"):
            last = "7"
            break
        elif used.startswith("eight"):
            last = "8"
            break
        elif used.startswith("nine"):
            last = "9"
            break
            
    num = int(first + last)
    res += num

print(res)
