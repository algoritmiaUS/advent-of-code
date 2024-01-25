
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


with open("./2022/day_01/input/input.txt") as f:
    maxi = 0
    sumi = 0
    for line in f:
        if line[:-1].isnumeric():
            sumi += int(line)
        else:
            if sumi > maxi:
                maxi = sumi
            sumi = 0

print(maxi)

with open("./2022/day_01/input/output_1.txt", "w") as f:
    f.write(f"{maxi}\n")
