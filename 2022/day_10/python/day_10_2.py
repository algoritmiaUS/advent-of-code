
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


cycle = 0
x = 1
sol = [[] for _ in range(6)]
with open("./2022/day_10/input/input.txt") as f:

    for line in f:
        i = cycle // 40
        j = cycle % 40
        cycle += 1

        # Draw character
        if abs(x - j) > 1:
            sol[i].append(".")
        else:
            sol[i].append("#")
        
        # Execute addx
        if line[0] == "a":
            i = cycle // 40
            j = cycle % 40
            cycle += 1

            # Draw extra character
            if abs(x - j) > 1:
                sol[i].append(".")
            else:
                sol[i].append("#")
            
            # Update x
            x += int(line[5:-1])
        

with open("./2022/day_10/input/output_2.txt", "w") as g:
    for ls in sol:
        line = "".join(ls)
        print(line)
        g.write(line + "\n")
