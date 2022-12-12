# Advent of Code 2022 - day 7 --- anthorne

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Directory:
    # Args: 0 = name, 1 = parent
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
            self.files = []
            self.parent_directory = None
            self.sub_folders = []
            self.total_size = 0
            self.is_working_dir = True
        if len(args) == 2:
            self.name = args[0]
            self.files = []
            self.parent_directory = args[1]
            self.sub_folders = []
            self.total_size = 0
            self.is_working_dir = False

    def calc_total_size(self):
        size = 0
        for f in self.files:
            size += f.size
        self.total_size = size


class Filesystem:
    def __init__(self, capacity):
        self.directories = []
        self.directories.append(Directory("/"))
        self.working_directory = self.directories[0]
        self.capacity = int(capacity)
        self.unused_space = 0

    def __str__(self):
        self.tree()
        return ""

    def calc_unused_space(self):
        self.unused_space = self.capacity - self.directories[0].total_size
        return self.unused_space

    def cd(self, dir):
        if dir == '/':
            self.working_directory = self.directories[0]
        elif dir == '..':
            if self.working_directory.parent_directory is not None:
                self.working_directory = self.working_directory.parent_directory
        else:
            for d in self.directories:
                if d.parent_directory == self.working_directory and d.name == dir:
                    self.working_directory = d

    def mkdir(self, dir):
        self.directories.append(Directory(dir, self.working_directory))
        self.working_directory.sub_folders.append(self.directories[-1])

    def add_size_to_parent_directory(self, dir, size):
        dir.total_size += int(size)
        if not dir == self.directories[0]:
            self.add_size_to_parent_directory(dir.parent_directory, size)

    def touch(self, f_name, f_size):
        self.working_directory.files.append(File(f_name, f_size))
        self.working_directory.total_size += int(f_size)
        if not self.working_directory == self.directories[0]:
            self.add_size_to_parent_directory(self.working_directory.parent_directory, f_size)

    def part_one(self, limit):
        t_size = 0
        for d in filesystem.directories:
            if d.total_size <= limit:
                t_size += d.total_size
        return t_size

    def part_two(self, d_size):
        directory_size = self.directories[0].total_size + 1
        for d in self.directories:
            if d_size <= d.total_size < directory_size:
                directory_size = d.total_size
        return directory_size

    def check_dir(self, dir):
        found = False
        for d in self.directories:
            if d.parent_directory == self.working_directory and d.name == dir:
                found = True
        if not found:
            self.mkdir(dir)

    def check_file(self, f_name, f_size):
        found = False
        for f in self.working_directory.files:
            if f.name == f_name:
                found = True
        if not found:
            self.touch(f_name, f_size)

    def pwd(self):
        print("$ pwd")
        folders = [self.working_directory.name]
        p = self.working_directory.parent_directory
        x = 1
        while x == 1:
            if p is None:
                x = 0
                break
            folders.append(p.name)
            p = p.parent_directory
        pwd_string = ""
        folders.reverse()
        first_time = True
        for i in folders:
            pwd_string += str(i)
            if not first_time:
                pwd_string += "/"
            first_time = False
        if len(pwd_string) == 1:
            print(str(pwd_string))
        else:
            print(str(pwd_string[:-1]))

    def sub_tree(self, dir):
        objects = []
        for s in dir.sub_folders:
            objects.append([s.name, 'dir', s.total_size])
            objects.append(self.sub_tree(s))
        for f in dir.files:
            objects.append([f.name, 'file', f.size])
        return objects

    def print_tree(self, objects, spacing):
        s = " " * spacing
        for o in objects:
            if type(o[0]) == list:
                spacing += 2
                self.print_tree(o, spacing)
            else:
                if o[1] == 'dir':
                    print(str(s) + "- " + str(o[0]) + " (dir) size=" + str(o[2]))
                elif o[1] == 'file':
                    print(str(s) + "  - " + str(o[0]) + " (file, size=" + str(o[2]) + ")")
                else:
                    print("something is not quite right....  DEBUG: " + str(o))

    def tree(self):
        objects = [self.sub_tree(self.directories[0])]
        print("- / (dir) size=" + str(self.directories[0].total_size))
        self.print_tree(objects, 0)
        return


filesystem = Filesystem(70000000)
current_command = ''
terminal_output = open("day7_input.txt", "r")
for line in terminal_output:
    l = line.strip().split(' ')
    if l[0] == '$':
        current_command = l[1]
        if len(l) == 3:
            current_argument = l[2]
        else:
            current_argument = ""
        if current_command == 'cd':
            filesystem.cd(current_argument)
            print('$ cd ' + str(current_argument))
            filesystem.pwd()
        if current_command == 'ls':
            print('$ ls')
    else:
        if current_command == 'ls':
            if l[0] == 'dir':
                # Directory
                directory = l[1]
                filesystem.check_dir(directory)
                print('dir ' + str(directory))
            else:
                # File
                file_size = l[0]
                file_name = l[1]
                filesystem.check_file(file_name, file_size)
                print(str(file_size) + ' ' + str(file_name))

print("--- File system ---")
print(filesystem)

print("- Part One - Find all of the directories with a total size of at most 100 000. "
      "What is the sum of the total sizes of those directories?")
part_one = filesystem.part_one(100000)
print("             Answer: " + str(part_one) + "\n")

# - Part two -
needed_space = 30000000

print(" - Total disk capacity: \t\t" + str(filesystem.capacity))
print(" - Total disk space: \t\t\t" + str(filesystem.directories[0].total_size))
print(" - Unused space needed: \t\t" + str(needed_space))
print(" - Unused space: \t\t\t\t" + str(filesystem.calc_unused_space()))
print(" - To be deleted (at least): \t " + str(needed_space - filesystem.unused_space) + "\n")

print("- Part Two - Find the smallest directory that, if deleted, would free up enough space on the "
      "filesystem to run the update. What is the total size of that directory?")
part_two = filesystem.part_two(needed_space - filesystem.unused_space)
print("             Answer: " + str(part_two))
