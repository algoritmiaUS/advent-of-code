
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


INITIAL_POINT = (500, 0)


def draw_lines(lines, abyss_threshold):
    mini = float("inf")
    maxi = float("-inf")
    for pair in lines:
        for x, _ in pair:
            if x < mini:
                mini = x
            if x > maxi:
                maxi = x

    for i in range(abyss_threshold+1):
        xs = [x for pair in lines for x, y in pair if y == i]
        j = mini
        while j <= maxi:
            if j in xs:
                print("#", end="")
                j += 1
                while j not in xs:
                    print("#", end="")
                    j += 1
                print("#", end="")
            else:
                print(".", end="")
            j += 1
        print()


def goes_to_abyss(
    lines: list, blocked: set, abyss_threshold: int, x: int, y: int
) -> bool:

    for candidate in ((x, y+1), (x-1, y+1), (x+1, y+1)):
        # Note: Candidate order enforces their priority

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

        if candidate[1] > abyss_threshold:
            return True
        else:
            return goes_to_abyss(lines, blocked, abyss_threshold, *candidate)

    # At this point, there are no admissible candidates
    blocked.add((x, y))
    return False


lines = []
abyss_threshold = 0
# with open("./2022/day_14/input/input_sample.txt") as f:
with open("./2022/day_14/input/input.txt") as f:

    for line in f:
        vertices = line.split(" -> ")  # Separate vertices data

        # Turn vertices into pairs of ints
        vertices = [tuple(map(int, v.split(","))) for v in vertices]

        maxi = max(v[1] for v in vertices)
        if maxi > abyss_threshold:
            abyss_threshold = maxi

        # Each line consists of a pair of vertices
        lines += list(zip(vertices, vertices[1:]))

sol = 0
blocked = set()
while not goes_to_abyss(lines, blocked, abyss_threshold, *INITIAL_POINT):
    sol += 1

print(sol)

with open("./2022/day_14/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
