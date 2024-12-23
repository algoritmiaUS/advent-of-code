"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

import re


def compute_muls(text: str) -> int:
    return sum(map(
        lambda x: int(x[0]) * int(x[1]),
        re.findall(r"mul\((\d+),(\d+)\)", text))
    )


with open("./2024/day_03/input/input_pablodavila.txt") as f:
    text = f.read()

partes = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", text)
counting = True
solution = 0
for parte in partes:
    if parte == "do()":
        counting = True
    elif parte == "don't()":
        counting = False
    elif counting:
        x, y = parte.split(",")
        x = int(x[4:])
        y = int(y[:-1])
        solution += x * y

print(solution)

with open("./2024/day_03/input/output_pablodavila_2.txt", "w") as f:
    f.write(f"{solution}\n")
