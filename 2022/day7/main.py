from heapq import *
class Directory:
    def __init__(self, name, parent, subdirectories, files):
        self.parent = parent
        self.name = name
        self.subdirectories = subdirectories 
        self.files = files

    def add_subdirectory(self, name):
        if name not in self.subdirectories:
            self.subdirectories[name] = Directory(name, self, {}, {})

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = File(name, size)

    def get_sub(self, name):
        return self.subdirectories[name]

    def get_parent(self):
        return self.parent

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

with open("input.txt", "r") as f:
    lines = f.readlines()
    start = 0
    first = lines[start].split(" ")
    parent = Directory(first[2], None, {}, {})
    current_dir = parent
    start += 1

    while start < len(lines):
        if lines[start].startswith("$"):
            cmds = lines[start].split(" ")
            cmd = cmds[1].strip()

            if cmd == "cd":
                arg = cmds[2].strip()

                if arg == "..": 
                    current_dir = current_dir.get_parent()
                elif arg == "/":
                    current_dir = parent
                else:
                    current_dir = current_dir.get_sub(arg)
        else:
            if lines[start].startswith("dir"):
                ln = lines[start].split(" ")
                name = ln[1].strip()
                current_dir.add_subdirectory(name)
            else:
                ln = lines[start].split(" ")
                size = ln[0]
                name = ln[1].strip()
                current_dir.add_file(name, size)

        start += 1

    sizes = {}
    heap = []
    def get_size(dir):
        global heap
        if dir == None:
            return 0

        size = 0 
        for item in dir.files.values():
            size += int(item.size)
        for item in dir.subdirectories.values():
            size += get_size(item)
        
        heappush(heap, size)
        return size
    
    under_10k = 0
    def printFiles(dir):
        if dir == None:
            return

        for item in dir.subdirectories.values():
            global under_10k
            size = get_size(item)
            if size < 100000:
                under_10k += size
            printFiles(item)

    printFiles(parent)
    print(under_10k)
    unused = 70000000 - get_size(parent)  
    needed = 30000000 - unused

    i = heappop(heap)
    while (i < needed):
        i = heappop(heap)
    print(i)
