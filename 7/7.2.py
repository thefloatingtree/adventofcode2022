import itertools

class File:
    def __init__(self, name, size) -> None:
        self.file_name = name
        self.size = size

    def __str__(self) -> None:
        return f"File '{self.file_name}' ({self.size})"


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child_directories = []
        self.child_files = []
        self.size = None

    def add_parent(self, parent):
        self.parent = parent

    def add_directory(self, directory):
        directory.add_parent(self)
        self.child_directories.append(directory)

    def get_directory(self, name):
        return list(filter(lambda dir: dir.name == name, self.child_directories))[0]

    def add_file(self, file):
        self.child_files.append(file)

    def calculate_size(self):
        if self.size == None:
            size = (
                sum(map(lambda file: file.size, self.child_files)) + 
                sum(map(lambda dir: dir.calculate_size(), self.child_directories))
            )
            self.size = size
        return self.size

    def find_root(self):
        if self.parent == None:
            return self
        return self.parent.find_root()

    def flatten(self):
        if len(self.child_directories) == 0:
            return [self]
        
        flattened_children = [self]
        for child in self.child_directories:
            flattened_children = list(itertools.chain(flattened_children, child.flatten()))

        return flattened_children
        
    def __str__(self) -> str:
        parent_name = self.parent.name if self.parent else "None"
        return f"Directory '{parent_name}' -> '{self.name}' ({len(self.child_directories)} child dirs)({len(self.child_files)} files)"


def cd(argument, current_directory: Directory):
    if argument == '..':
        return current_directory.parent
    else:
        return current_directory.get_directory(argument)


def ls(lines, start_line_index, current_directory: Directory):
    line_index = start_line_index
    line_index_in_range = line_index < len(lines)
    while line_index_in_range and lines[line_index][0] != '$':
        [dir_or_size, name] = lines[line_index].split(' ')
        if dir_or_size == 'dir':
            current_directory.add_directory(Directory(name))
        else:
            size = int(dir_or_size)
            current_directory.add_file(File(name, size))
        line_index += 1
        line_index_in_range = line_index < len(lines)
    return current_directory


with open('input.txt') as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))[1:]

    current_directory = Directory('/')

    for line_index, line in enumerate(lines):
        if line[0] == '$':
            command = line.split(' ')[1]
            argument = None if 2 >= len(line.split(' ')) else line.split(' ')[2]
            match command:
                case 'cd':
                    current_directory = cd(argument, current_directory)
                case 'ls':
                    current_directory = ls(lines, line_index + 1, current_directory)

    root_directory = current_directory.find_root()
    root_directory.calculate_size()

    directories = root_directory.flatten()
    directories.sort(key=lambda dir: dir.size)

    unused_space = 70000000 - root_directory.size
    update_size = 30000000

    required_size_delta = unused_space - update_size

    if required_size_delta > 0:
        exit()

    required_size_limit = abs(required_size_delta)

    for directory in directories:
        if directory.size >= required_size_limit:
            print(directory.size)
            break


