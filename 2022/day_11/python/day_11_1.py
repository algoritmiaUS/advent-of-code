
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


import heapq
from typing import Callable


class Monkey:

    def __init__(
            self,
            starting_items: list,
            operation: Callable,
            test: Callable,
            target_true: int,
            target_false: int):

        self.items = starting_items
        self.operation = operation
        self.test = test
        self.target_true = target_true
        self.target_false = target_false
        self.inspection_count = 0

    def turn(self) -> dict:
        res = {
            self.target_true: [],
            self.target_false: [],
        }

        for item in self.items:
            new = self.operation(item)
            if self.test(new):
                res[self.target_true].append(new)
            else:
                res[self.target_false].append(new)
        
        self.inspection_count += len(self.items)
        self.items = []

        return res
    
    def __str__(self):
        return f"{self.items=}\n{self.inspection_count=}"


def build_operation(expression: str):
    a, op, b = expression.split()
    
    if op == "+":
        op = lambda x, y: x + y
    else:
        op = lambda x, y: x * y
    
    if a == "old":
        a = lambda old: old
    else:
        val = int(a)
        a = lambda _: val
    
    if b == "old":
        b = lambda old: old
    else:
        val = int(b)
        b = lambda _: val
    
    return lambda old: op(a(old), b(old)) // 3


def build_test(n: int):
    return lambda x: x % n == 0


# Read monkeys data
monkeys = []
with open("./2022/day_11/input/input.txt") as f:
    for line in f:

        # Starting numbers
        line = next(f)
        starting_items = list(map(int, line[18:].split(", ")))

        # Operation
        line = next(f)
        operation = build_operation(line[19:])

        # Test
        line = next(f)
        n = int(line[21:-1])
        test = build_test(n)

        # Targets
        target_true = int(next(f)[29:-1])
        target_false = int(next(f)[30:-1])

        monkeys.append(Monkey(
            starting_items,
            operation,
            test,
            target_true,
            target_false
        ))

        next(f)

# Run 20.000 rounds
for _ in range(20):
    for i,m in enumerate(monkeys):
        throws = m.turn()
        for i in throws:
            monkeys[i].items += throws[i]

a, b = heapq.nlargest(2, [m.inspection_count for m in monkeys])
sol = a * b
print(sol)

with open("./2022/day_11/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
