"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

import re


with open("./2024/day_03/input/input_pablodavila.txt") as f:
    text = f.read()

solution = sum(map(
    lambda x: int(x[0]) * int(x[1]),
    re.findall(r"mul\((\d+),(\d+)\)", text))
)

print(solution)

with open("./2024/day_03/input/output_pablodavila_1.txt", "w") as f:
    f.write(f"{solution}\n")
