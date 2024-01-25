
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


def search(ls:list, v):
    res = None
    for i, e in enumerate(ls):
        if e == v:
            res = i
    return res


with open("./2022/day_06/input/input.txt") as f:
    data = next(f)

queue = list(data[:3])
for i, l in enumerate(data[3:], 3):

    # Detect an remove duplicate
    j = search(queue, l)
    if j is not None:
        queue[:j+1] = []

    # Update queue and check if the objective has been reached
    queue.append(l)
    if len(queue) == 14:
        sol = i +1
        break

print(sol)

with open("./2022/day_06/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
