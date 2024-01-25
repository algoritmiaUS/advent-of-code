
# Solution by Pablo Dávila Herrero (https://pablodavila.eu)



class dir:

    def __init__(self, size=0):
        self.children = {}
        self.size = size
        self.updated_size = False

    def add_dir(self, name):
        if name not in self.children:
            self.children[name] = dir()

    def add_file(self, name, size):
        if name not in self.children:
            self.children[name] = size
            self.size += size

    def get_size(self):
        if not self.updated_size:
            self.size += sum(c.get_size() for c in self.children.values() if isinstance(c,dir))
            self.updated_size = True
        return self.size

    def __getitem__(self, name):
        return self.children[name]


# Construct file system structure
# (probably useful for part 2, too)
with open("./2022/day_07/input/input.txt") as f:
    stack = []
    root = dir()
    current = None
    for line in f:
        if line.startswith("$ cd /"):
            current = root
            stack = []
        elif line.startswith("$ cd .."):
            current = stack.pop()
        elif line.startswith("$ cd"):
            stack.append(current)
            name = line[5:-1]
            current = current[name]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            name = line[4:-1]
            current.add_dir(name)
        else:
            size, name = line.split()
            current.add_file(name, int(size))

# Seach for the requested directories (DFS)
sol = 0
search = [root]
while len(search) != 0:
    _dir = search.pop()
    if _dir.get_size() <= 100_000:
        sol += _dir.get_size()
    search += [c for c in _dir.children.values() if isinstance(c,dir)]

print(sol)

with open("./2022/day_07/input/output_1.txt", "w") as f:
    f.write(f"{sol}\n")
