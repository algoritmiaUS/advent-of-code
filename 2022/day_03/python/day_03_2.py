
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


import string


priorities = {l:i for i,l in enumerate(string.ascii_letters, 1)}

sumi = 0
with open("./2022/day_03/input/input.txt") as f:
    for line in f:
        sumi += priorities[list(set(line[:-1]) & set(next(f)) & set(next(f)))[0]]
        

print(sumi)

with open("./2022/day_03/input/output_2.txt", "w") as f:
    f.write(f"{sumi}\n")
