#!/usr/bin/env python3

def adv6_1():
    pass

def main():
    lantern_data = []
    with open("lanternfish_data.txt") as f:
        lantern_data = f.readlines()
    f.close

    #read text as numbers
    #loop over data set
    #decrease by 1 for each loop (day)
    #when value is 0, set to 7 and append one set to 9 and go one more day.
    #   in this way when we get to the next day it will be a 6 and an 8 after decrease
    #after 80 days, count all "fish" and exclude the 9s
    #either do a for index in range(80), while days < 80 or recursive with day count passed
    #write tests

    print("part 1 - number of lanternfish:", adv6_1())
    #print("part 2 - :", adv6_2())

if __name__ == '__main__':
    main()
