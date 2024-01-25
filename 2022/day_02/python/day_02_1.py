
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


sumi = 0
with open("./2022/day_02/input/input.txt") as f:
    for line in f:
        elf, me = line[0], line[2]

        if me == "X":
            sumi += 1
            if elf == "A":
                sumi += 3
            elif elf == "C":
                sumi += 6
        elif me == "Y":
            sumi += 2
            if elf == "A":
                sumi += 6
            elif elf == "B":
                sumi += 3
        else:
            sumi += 3
            if elf == "B":
                sumi += 6
            elif elf == "C":
                sumi += 3

print(sumi)

with open("./2022/day_02/input/output_1.txt", "w") as f:
    f.write(f"{sumi}\n")
