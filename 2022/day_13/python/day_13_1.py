
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


import json
from typing import Union


def ordered(left: Union[list, int], right: Union[list, int]) -> bool:

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        for l, r in zip(left, right):
            res = ordered(l, r)
            if res is not None:
                return res

        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)


sol = 0
with open("./2022/day_13/input/input.txt") as f:

    for i, line in enumerate(f, 1):
        left = json.loads(line)
        right = json.loads(next(f))

        if ordered(left, right):
            sol += i

        next(f)  # Discard empty line

print(sol)

with open("./2022/day_13/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
