
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


cycle = 1
x = 1
sol = 0
with open("./2022/day_10/input/input.txt") as f:

    updated = False
    addition = 0
    for line in f:

        # Update sol
        if cycle % 40 == 20:
            sol += x * cycle
            updated = True
        elif (cycle % 40 == 21) and not updated:
            sol += (x - addition) * cycle
        else:
            updated = False

        # Execute noop
        if line[0] == "n":
            addition = 1

        # Execute addx
        else:
            x += int(line[5:-1])
            addition = 2
        cycle += addition

print(sol)

with open("./2022/day_10/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
