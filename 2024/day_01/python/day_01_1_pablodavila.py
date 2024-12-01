"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

ls1 = []
ls2 = []
with open("./2024/day_01/input/input.txt") as f:
    for line in f:
        n1, n2 = list(map(int, line.split()))
        ls1.append(n1)
        ls2.append(n2)

ls1.sort()
ls2.sort()

sumi = 0
for n1, n2 in zip(ls1, ls2):
    sumi += abs(n1 - n2)

print(sumi)

with open("./2024/day_01/input/output_1.txt", "w") as f:
    f.write(f"{sumi}\n")
