
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


sumi = 0
with open("./2022/day_04/input/input.txt") as f:
    for line in f:
        ranges = line.split(",")
        a, b = tuple(map(int, ranges[0].split("-")))
        c, d = tuple(map(int, ranges[1].split("-")))
        if a<=c and d<=b or c<=a and b<=d:
            sumi += 1

print(sumi)

with open("./2022/day_04/input/output_1.txt", "w") as f:
    f.write(f"{sumi}\n")
