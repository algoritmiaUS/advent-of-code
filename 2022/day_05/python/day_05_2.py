
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


with open("./2022/day_05/input/input.txt") as f:
    data = [[] for _ in range(9)]
    for i, line in enumerate(f):
        for j in range(1, len(line), 4):
            if line[j] != ' ':
                data[j//4].insert(0, line[j])
        if i == 7:
            break
    
    next(f)
    next(f)

    for line in f:
        parts = line.split()
        n = int(parts[1])
        i = int(parts[3]) - 1
        j = int(parts[5]) - 1

        data[j] += data[i][-n:]
        data[i][-n:] = []


sol = "".join([col[-1] for col in data if len(col)!=0])

print(sol)

with open("./2022/day_05/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
