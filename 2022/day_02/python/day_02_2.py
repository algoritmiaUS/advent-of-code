
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


sumi = 0
with open("./2022/day_02/input/input.txt") as f:
    for line in f:
        elf, me = line[0], line[2]

        if me == "X":
            if elf == "A":
                sumi += 3
            elif elf == "B":
                sumi += 1
            else:
                sumi += 2
        elif me == "Y":
            sumi += 3
            if elf == "A":
                sumi += 1
            elif elf == "B":
                sumi += 2
            else:
                sumi += 3
        else:
            sumi += 6
            if elf == "A":
                sumi += 2
            elif elf == "B":
                sumi += 3
            else:
                sumi += 1

print(sumi)

with open("./2022/day_02/input/output_2.txt", "w") as f:
    f.write(f"{sumi}\n")
