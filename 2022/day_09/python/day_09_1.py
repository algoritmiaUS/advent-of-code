
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


# Initial position of both head and tail
hx = hy = tx = ty = 0
past_positions = {(0,0)}

with open("./2022/day_09/input/input.txt") as f:

    for line in f:
        dir, steps = line.split()
        for _ in range(int(steps)):
            if dir == 'L':
                if hx < tx:
                    tx -= 1
                    ty = hy
                hx -= 1
            elif dir == 'R':
                if tx < hx:
                    tx += 1
                    ty = hy
                hx += 1
            elif dir == 'U':
                if ty < hy:
                    ty += 1
                    tx = hx
                hy += 1
            else:
                if hy < ty:
                    ty -= 1
                    tx = hx
                hy -= 1
            past_positions.add((tx,ty))

sol = len(past_positions)
print(sol)

with open("./2022/day_09/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
