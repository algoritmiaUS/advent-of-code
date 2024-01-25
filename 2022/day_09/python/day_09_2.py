
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


def update_knots(pos):
    # Updates the position of all the knots and returns the tail position

    for i in range(1, len(pos)):
        hx, hy = pos[i-1]
        tx, ty = pos[i]

        if hx < tx - 1:
            tx -= 1
            if hy < ty:
                ty -= 1
            elif ty < hy:
                ty += 1
        elif tx + 1 < hx:
            tx += 1
            if hy < ty:
                ty -= 1
            elif ty < hy:
                ty += 1
        elif hy < ty - 1:
            ty -= 1
            if hx < tx:
                tx -= 1
            elif tx < hx:
                tx += 1
        elif ty + 1 < hy:
            ty += 1
            if hx < tx:
                tx -= 1
            elif tx < hx:
                tx += 1
        else:
            break

        pos[i] = (tx, ty)

    return pos[-1]  # Tail position


history = set()
rope_pos = [(0, 0) for _ in range(10)]
# with open("./2022/day_09/input/input_sample.txt") as f:  # TEMP
with open("./2022/day_09/input/input.txt") as f:  # TEMP
    # c = 0
    for line in f:
        dir, steps = line.split()
        for _ in range(int(steps)):
            if dir == 'L':
                rope_pos[0] = (rope_pos[0][0]-1, rope_pos[0][1])
            elif dir == 'R':
                rope_pos[0] = (rope_pos[0][0]+1, rope_pos[0][1])
            elif dir == 'U':
                rope_pos[0] = (rope_pos[0][0], rope_pos[0][1]+1)
            else:
                rope_pos[0] = (rope_pos[0][0], rope_pos[0][1]-1)
            history.add(update_knots(rope_pos))
        # print(rope_pos)  # TEMP
        # c += 1
        # if c == 10:
        #     break

sol = len(history)
print(sol)

with open("./2022/day_09/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
