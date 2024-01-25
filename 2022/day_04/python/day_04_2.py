
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


'''
a c b d
c a d b
a c d b
c a b d
'''


sumi = 0
with open("./2022/day_04/input/input.txt") as f:
    for line in f:
        ranges = line.split(",")
        a, b = tuple(map(int, ranges[0].split("-")))
        c, d = tuple(map(int, ranges[1].split("-")))
        if a<=c and c<=b or c<=a and a<=d:
            sumi += 1

print(sumi)

with open("./2022/day_04/input/output_2.txt", "w") as f:
    f.write(f"{sumi}\n")
