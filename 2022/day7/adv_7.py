#!/usr/bin/env python3

from typing import List


class Folder:
    def __init__(self, dir_name: str, content: List[any] = []):
        self.dir_name = dir_name
        self.content = content

class File:
    def __init__(self, file_name: str, size: int):
        self.file_name = file_name
        self.size = size

def adv7_1() -> int:
    return


def adv7_2() -> int:
    return


def make_file_system() -> Folder:
    return

def main():

    file_system_data = []
    with open("file_system.txt") as f:
        file_system_data = f.read().splitlines()
    f.close()

    # a = Folder("a")
    # a.content.append(Folder("f"))
    # print(type(a.content[0]))

    print(file_system_data)

    print("part 1 - :", adv7_1())
    print("part 2 - :", adv7_2())


if __name__ == '__main__':
    main()

