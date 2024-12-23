"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

from collections import defaultdict
import functools


left_rules = defaultdict(set)
right_rules = defaultdict(set)

solution = 0
with open("./2024/day_05/input/input.txt") as f:
    for line in f:
        if line == "\n":
            break

        x, y = list(map(int, line.strip().split("|")))
        right_rules[x].add(y)
        left_rules[y].add(x)

    not_good_orders = []
    for line in f:
        good = True
        ls = list(map(int, line.strip().split(",")))
        for i, x in enumerate(ls):
            for y in ls[i+1:]:
                if x in right_rules[y] or y in left_rules[x]:
                    good = False
                    break
            if not good:
                break
        if not good:
            not_good_orders.append(ls)

for ls in not_good_orders:
    ls.sort(key=functools.cmp_to_key(lambda x, y: 1 if x in right_rules[y] or y in left_rules[x] else -1))
    solution += ls[len(ls) // 2]

print(solution)

with open("./2024/day_05/input/output_2.txt", "w") as f:
    f.write(f"{solution}\n")
