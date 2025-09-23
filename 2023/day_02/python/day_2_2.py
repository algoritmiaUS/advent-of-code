
import sys


INPUT_PATH = "day_2\input.txt"
if len(sys.argv) > 1:
    INPUT_PATH = sys.argv[1]

with open(INPUT_PATH) as f:
    data = f.readlines()


res = 0
for line in data:
    game, game_info = line.split(":")
    maxi = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for peek_info in game_info.split("; "):
        for cubes_info in peek_info.split(","):
            n, color = cubes_info.split()
            n = int(n)
            if maxi[color] < n:
                maxi[color] = n
    res += maxi["red"] * maxi["green"] * maxi["blue"]

print(res)
