
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


data = []
with open("./2022/day_08/input/input.txt") as f:
    for line in f:
        data.append(list(map(int, line[:-1])))

visibles = set()
n = len(data)

maxis = [-1 for _ in range(n)]
for i in range(n):
    for j in range(n):
        h = data[i][j]
        if h > maxis[j]:
            visibles.add((i,j))
            maxis[j] = h

maxis = [-1 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n):
        h = data[i][j]
        if h > maxis[j]:
            visibles.add((i,j))
            maxis[j] = h

maxis = [-1 for _ in range(n)]
for j in range(n):
    for i in range(n):
        h = data[i][j]
        if h > maxis[i]:
            visibles.add((i,j))
            maxis[i] = h

maxis = [-1 for _ in range(n)]
for j in range(n-1, -1, -1):
    for i in range(n):
        h = data[i][j]
        if h > maxis[i]:
            visibles.add((i,j))
            maxis[i] = h

sol = len(visibles)
print(sol)

with open("./2022/day_08/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
