"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

solution = 0
text = []
text_t = [[] for _ in range(140)]
with open("./2024/day_04/input/input.txt") as f:
    for line in f:
        solution += line.count("XMAS") + line.count("SAMX")

        text.append(line.strip())
        for d, c in zip(text_t, line):
            d.append(c)
text_t = ["".join(d) for d in text_t]

for line in text_t:
    solution += line.count("XMAS") + line.count("SAMX")

for i in range(len(text) - 3):
    for j in range(len(text[i]) - 3):
        if text[i][j] == "X" and text[i + 1][j + 1] == "M" and text[i + 2][j + 2] == "A" and text[i + 3][j + 3] == "S":
            solution += 1
        elif text[i][j] == "S" and text[i + 1][j + 1] == "A" and text[i + 2][j + 2] == "M" and text[i + 3][j + 3] == "X":
            solution += 1

for i in range(len(text)-1, 2, -1):
    for j in range(len(text[i]) - 3):
        if text[i][j] == "X" and text[i - 1][j + 1] == "M" and text[i - 2][j + 2] == "A" and text[i - 3][j + 3] == "S":
            solution += 1
        elif text[i][j] == "S" and text[i - 1][j + 1] == "A" and text[i - 2][j + 2] == "M" and text[i - 3][j + 3] == "X":
            solution += 1

print(solution)

with open("./2024/day_04/input/output_1.txt", "w") as f:
    f.write(f"{solution}\n")
