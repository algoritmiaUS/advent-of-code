
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


import functools
import json
from typing import Union


def cmp_packets(left: Union[list, int], right: Union[list, int]) -> bool:

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        for l, r in zip(left, right):
            res = cmp_packets(l, r)
            if res != 0:
                return res

        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0


packets = [[[2]], [[6]]]
with open("./2022/day_13/input/input.txt") as f:

    for i, line in enumerate(f, 1):
        packets.append(json.loads(line))
        packets.append(json.loads(next(f)))

        next(f)  # Discard empty line

packets.sort(key=functools.cmp_to_key(cmp_packets))
sol = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(sol)

with open("./2022/day_13/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
