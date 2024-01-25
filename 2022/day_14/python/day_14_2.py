
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


INITIAL_POINT = (500, 0)


def reaches_source(
    lines: list, blocked: set, bottom: int, x: int, y: int
) -> bool:

    for candidate in ((x, y+1), (x-1, y+1), (x+1, y+1)):
        # Note: Candidate order enforces their priority

        # Check if (x,y) is at the bottom
        if y == bottom:
            blocked.add((x, y))
            return False

        # Check if the candidate is blocked
        if candidate in blocked:
            continue

        # Check if the candidate is part of a rock
        admissible = True
        for (a0, a1), (b0, b1) in lines:
            if (
                (a0 <= candidate[0] <= b0 or b0 <= candidate[0] <= a0)
                and (a1 <= candidate[1] <= b1 or b1 <= candidate[1] <= a1)
            ):
                admissible = False
                break

        if not admissible:
            continue
        else:
            reaches_source(lines, blocked, bottom, *candidate)
            return False

    # At this point, there are no admissible candidates
    if (x,y) == INITIAL_POINT:
        return True
    else:
        blocked.add((x, y))
        return False


lines = []
bottom = 0
# Needed to draw final state
# min_x = 500  # TEMP
# max_x = 500  # TEMP
# with open("./2022/day_14/input/input_sample.txt") as f:
with open("./2022/day_14/input/input.txt") as f:

    for line in f:
        vertices = line.split(" -> ")  # Separate vertices data

        # Turn vertices into pairs of ints
        vertices = [tuple(map(int, v.split(","))) for v in vertices]

        maxi = max(v[1] for v in vertices)
        if maxi > bottom:
            bottom = maxi

        # Needed to draw final state
        # maxi = max(v[0] for v in vertices)  # TEMP
        # mini = min(v[0] for v in vertices)  # TEMP
        # if maxi > max_x:  # TEMP
        #     max_x = maxi  # TEMP
        # if mini < min_x:  # TEMP
        #     min_x = mini  # TEMP

        # Each line consists of a pair of vertices
        lines += list(zip(vertices, vertices[1:]))
    
bottom += 1

sol = 1  # The initial position is not counted later
blocked = set()
while not reaches_source(lines, blocked, bottom, *INITIAL_POINT):
    sol += 1

# Draw final state
# for i in range(bottom+3):  # TEMP
#     print(f"{i:3d}", end="")
#     for j in range(min_x-10, max_x+11):
#         if i==0 and j==500:
#             print("s", end="")
#         elif (j, i) in blocked:
#             print("o", end="")
#         elif any(
#                 (a0 <= j <= b0 or b0 <= j <= a0)
#                 and (a1 <= i <= b1 or b1 <= i <= a1)
#                 for (a0,a1), (b0,b1) in lines
#             ):
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

print(sol)

with open("./2022/day_14/input/output_2.txt", "w") as f:
    f.write(f"{sol}\n")
