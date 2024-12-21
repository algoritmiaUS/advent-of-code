"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

lines = []
with open("./2024/day_04/input/input.txt") as f:
    for line in f:
        lines.append(line.strip())

solution = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        if lines[i][j] != "A":
            continue

        if (
            {lines[i-1][j-1], lines[i+1][j+1]} == {"M", "S"}
            and {lines[i+1][j-1], lines[i-1][j+1]} == {"M", "S"}
        ):
            solution += 1


print(solution)

with open("./2024/day_04/input/output_2.txt", "w") as f:
    f.write(f"{solution}\n")
