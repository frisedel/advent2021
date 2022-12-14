#!/usr/bin/env python3

from collections import defaultdict
import pathlib
from typing import List

root = pathlib.Path("/")


def adv7_1(filesystem: defaultdict(int)) -> int:
    return sum(size for size in filesystem.values() if size <= 100000)


def adv7_2(filesystem: defaultdict(int)) -> int:
    return min(size for size in filesystem.values() if size >= filesystem.get(root) - 40000000)


def make_file_system(files_data: List[str]):
    filesystem, cwd = defaultdict(int), root

    for line in files_data:
        if line.startswith("$ cd"):
            path_arg = line.split()[-1]
            cwd = {
                "/": root,
                "..": cwd.parent,
            }.get(path_arg, cwd / path_arg)
        elif line[0].isdigit():
            file_path = cwd / line.split()[1]
            while file_path != pathlib.Path("/"):
                file_path = file_path.parent
                filesystem[file_path] += int(line.split()[0])
    return filesystem

def main():

    filesystem_data = []
    with open("filesystem.txt") as f:
        filesystem_data = f.read().splitlines()
    f.close()

    filesystem = make_file_system(filesystem_data)

    print("part 1 - Total size of folders under 10000:", adv7_1(filesystem))
    print("part 2 - Size of smallest folder to delete:", adv7_2(filesystem))


if __name__ == '__main__':
    main()

