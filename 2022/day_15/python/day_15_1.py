
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)


# TARGET_COLUMN = 10  # Sample target
TARGET_COLUMN = 2_000_000


sensors = []
beacons = {}
# with open("./2022/day_15/input/input_sample.txt") as f:
with open("./2022/day_15/input/input.txt") as f:

    for line in f:
        s0, s1_b0, b1 = line.split(", ")
        s0 = int(s0[12:])
        s1 = int(s1_b0[2:s1_b0.index(":")])
        b0 = int(s1_b0[s1_b0.index("=", 27) + 1:])
        b1 = int(b1[2:])

        # Store position and radius of the beacon
        sensors.append((s0, s1, abs(s0-b0) + abs(s1-b1)))

        # Store beacon positions indexed by row
        if b1 in beacons:
            beacons[b1].add(b0)
        else:
            beacons[b1] = {b0}

# Compute the intervals resulting of intersecting
# sensor scanned areas with the target column
scanned_intervals = []
for s0, s1, r in sensors:
    r2 = r - abs(TARGET_COLUMN - s1)
    if r2 < 0:
        continue
    else:
        scanned_intervals.append((s0-r2, s0+r2))

# Compute the intersection of all scanned intervals
scanned_intervals.sort()  # n·log(n) is better than n^2
sol = -len(beacons.get(TARGET_COLUMN, 0))  # Discard postions with beacons
i = 0
while True:
    left = scanned_intervals[i][0]
    right = scanned_intervals[i][1]
    for j in range(i+1, len(scanned_intervals)):
        if scanned_intervals[j][0] <= right:
            if right < scanned_intervals[j][1]:
                right = scanned_intervals[j][1]
        else:
            break
    else:  # no break -> end reached by j
        sol += right - left + 1
        break

    sol += right - left + 1
    i = j

print(sol)

with open("./2022/day_15/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
