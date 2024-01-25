
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


with open("./2022/day_06/input/input.txt") as f:
    data = next(f)

for i in range(3, len(data)):
    a, b, c, d = data[i-3:i+1]
    found = all((
        a != b,
        b != c,
        c != d,
        d != a,
        a != c,
        b != d
    ))
    if found:
        sol = i + 1
        break

print(sol)

with open("./2022/day_06/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
