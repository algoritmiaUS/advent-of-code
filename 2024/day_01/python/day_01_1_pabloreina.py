with open("./2024/day_01/input/input.txt") as f:
    lineas = []

    for linea in f:
        linea = list(map(int,linea.split()))
        lineas.append(linea)

lineas1 = list(map(lambda x: x[0], lineas))
lineas2 = list(map(lambda x: x[1], lineas))


lineas1.sort()
lineas2.sort()

contador = 0

for x, y in zip(lineas1, lineas2):
    contador += abs(x - y)

print(contador)
    