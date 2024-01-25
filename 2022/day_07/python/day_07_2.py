
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
            self.size += sum(c.get_size()
                             for c in self.children.values() if isinstance(c, dir))
            self.updated_size = True
        return self.size

    def __getitem__(self, name):
        return self.children[name]


# Construct file system structure
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

# Seach for the requested directory (DFS)
search = [c for c in root.children.values() if isinstance(c, dir)]
mini = root.get_size()
objective = 30_000_000 - (70_000_000 - root.get_size())
while len(search) != 0:
    _dir = search.pop()
    if objective <= _dir.get_size():
        if _dir.get_size() < mini:
            mini = _dir.get_size()
        search += [c for c in _dir.children.values() if isinstance(c, dir)]

print(mini)

with open("./2022/day_07/input/output_2.txt", "w") as f:
    f.write(f"{mini}\n")
