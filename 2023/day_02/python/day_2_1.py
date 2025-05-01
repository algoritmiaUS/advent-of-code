"""
Determine which games would have been possible if the bag had been loaded with only 12
red cubes, 13 green cubes, and 14 blue cubes.
"""


import sys


INPUT_PATH = "day_2\input.txt"
if len(sys.argv) > 1:
    INPUT_PATH = sys.argv[1]

with open(INPUT_PATH) as f:
    data = f.readlines()


limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}
res = 0
for line in data:
    game, game_info = line.split(":")
    num = int(game.split()[1])
    valid = True
    for peek_info in game_info.split("; "):
        for cubes_info in peek_info.split(","):
            n, color = cubes_info.split()
            if limit[color] < int(n):
                valid = False
                break
        if valid == False:
            break
    else:
        res += num

print(res)
