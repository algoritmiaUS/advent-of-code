"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

from collections import defaultdict


left_rules = defaultdict(set)
right_rules = defaultdict(set)

solution = 0
with open("./2024/day_05/input/input.txt") as f:
    for line in f:
        if line == "\n":
            break

        x, y = list(map(int, line.strip().split("|")))
        right_rules[x].add(y)

    for line in f:
        good = True
        ls = list(map(int, line.strip().split(",")))
        for i, x in enumerate(ls):
            for y in ls[i+1:]:
                if x in right_rules[y]:
                    good = False
                    break
            if not good:
                break
        if not good:
            solution += ls[len(ls) // 2]

print(solution)

with open("./2024/day_05/input/output_1.txt", "w") as f:
    f.write(f"{solution}\n")
