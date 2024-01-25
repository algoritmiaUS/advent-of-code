
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


data = []
with open("./2022/day_08/input/input.txt") as f:
    for line in f:
        data.append(list(map(int, line[:-1])))

n = len(data)

up = [[] for _ in range(n)]
for j in range(n):
    view = {h: 0 for h in range(10)}
    for i in range(n):
        up[i].append(view[data[i][j]])
        for h in range(10):
            if data[i][j] < h:
                view[h] += 1
            else:
                view[h] = 1

down = [[] for _ in range(n)]
for j in range(n):
    view = {h: 0 for h in range(10)}
    for i in range(n-1, -1, -1):
        down[i].append(view[data[i][j]])
        for h in range(10):
            if data[i][j] < h:
                view[h] += 1
            else:
                view[h] = 1

left = [[] for _ in range(n)]
for i in range(n):
    view = {h: 0 for h in range(10)}
    for j in range(n):
        left[i].append(view[data[i][j]])
        for h in range(10):
            if data[i][j] < h:
                view[h] += 1
            else:
                view[h] = 1

right = [[] for _ in range(n)]
for i in range(n):
    view = {h: 0 for h in range(10)}
    for j in range(n-1, -1, -1):
        right[i].append(view[data[i][j]])
        for h in range(10):
            if data[i][j] < h:
                view[h] += 1
            else:
                view[h] = 1

sol = max(
    up[i][j] * down[i][j] * left[i][j] * right[i][j]
    for i in range(n)
    for j in range(n)
)
print(sol)

with open("./2022/day_08/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
