"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

from typing import Counter


ls1 = set()
ls2 = Counter()
with open("./2024/day_01/input/input.txt") as f:
    for line in f:
        n1, n2 = list(map(int, line.split()))
        ls1.add(n1)
        ls2[n2] += 1

sumi = 0
for n in ls1:
    sumi += n * ls2[n]

print(sumi)

with open("./2024/day_01/input/output_2.txt", "w") as f:
    f.write(f"{sumi}\n")
