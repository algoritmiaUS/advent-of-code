from collections import Counter

with open("./2024/day_01/input/input.txt") as f:
    lineas = []

    for linea in f:
        linea = list(map(int,linea.split()))
        lineas.append(linea)

lineas1 = list(map(lambda x: x[0], lineas))
lineas2 = list(map(lambda x: x[1], lineas))


contador2 = Counter(lineas2)

contador = 0

for x in (lineas1):
    contador += x * contador2[x]

print(contador)
