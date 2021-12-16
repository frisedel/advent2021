#!/usr/bin/env python3

def adv10_1():
    pass

def adv10_2():
    pass

def main():
    input_data = []
    with open("syntax_input.txt") as f:
        input_data = f.readlines()
    f.close

    print("part 1 - :", adv10_1())
    print("part 2 - :", adv10_2())

if __name__ == '__main__':
    main()
