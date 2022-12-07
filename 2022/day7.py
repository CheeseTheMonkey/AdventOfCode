

from operator import attrgetter

# = open("day7.test")
f = open("day7.input")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return self.name

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        self.children = {}

    def add_child(self, child):
        if isinstance(child, (Dir, File)):
            self.children[child.name] = child

        else:
            raise TypeError

    @property
    def size(self):
        return sum((child.size for child in self.children.values()))

    def get_all_subdirectories(self):
        dirs = []
        for child in self.children.values():
            if isinstance(child, Dir):
                dirs.append(child)
                dirs.extend(child.get_all_subdirectories())
        return dirs
         

    def __str__(self):
        string = f'{self.name}\n'
        for child in self.children.values():
            string += f'{"  "*self.depth}{child.__str__()}'
        return string


root = Dir('/')
cwd = root

for line in f:
    line = line.strip()
    parts = line.split(' ')
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '/':
                cwd = root
            elif parts[2] == '..' and cwd.parent:
                cwd = cwd.parent
            else:
                cwd = cwd.children[parts[2]]

    elif parts[0] == 'dir':
        cwd.add_child(Dir(parts[1], cwd))
    elif parts[0][0].isdigit():
        cwd.add_child(File(parts[1], parts[0]))


dirs = [root]
dirs.extend(root.get_all_subdirectories())

print(f'Part 1: {sum(dir.size for dir in dirs if dir.size <= 100000)}')

available_space = 70000000 - root.size
required_space = 30000000 - available_space

dirs = sorted([d for d in dirs if d.size > required_space], key=attrgetter('size'))
print(f'Part2: {dirs[0].size}')
