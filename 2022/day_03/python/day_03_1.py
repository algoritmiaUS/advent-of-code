
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


import string


priorities = {l:i for i,l in enumerate(string.ascii_letters, 1)}

sumi = 0
with open("./2022/day_03/input/input.txt") as f:
    for line in f:
        mid = len(line)//2
        left = set(line[:mid])
        for l in line[mid:-1]:
            if l in left:
                sumi += priorities[l]
                break

print(sumi)

with open("./2022/day_03/input/output_1.txt", "w") as f:
    f.write(f"{sumi}\n")
