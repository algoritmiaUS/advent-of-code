
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


max1 = 0
max2 = 0
max3 = 0
sumi = 0

with open("./2022/day_01/input/input.txt") as f:
    for line in f:
        if line[:-1].isnumeric():
            sumi += int(line)
        else:
            if sumi > max1:
                max3 = max2
                max2 = max1
                max1 = sumi
            elif sumi > max2:
                max3 = max2
                max2 = sumi
            elif sumi > max3:
                max3 = sumi

            sumi = 0

sol = max1 + max2 + max3
print(sol)

with open("./2022/day_01/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
