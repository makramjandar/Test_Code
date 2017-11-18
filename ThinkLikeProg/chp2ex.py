#!/usr/local/bin/python
# Think Like a Programmer Chapter 2: Pure Puzzles exercises


def main():
    poundV()
    print()
    poundDiamond()


def poundV():
    '''
    Using only single output statements of a space, pound, or new line, create:
    ########
     ######
      ####
       ##
    '''
    n = 4
    space = ' '
    pound = '#'
    for i in range(n, 0, -1):
        print((space * (n - i)) + (pound * i * 2) + (space * (n - i)))


def poundDiamond():
    '''
    Using only single output statements of a space, pound, or new line, create:
       ##
      ####
     ######
    ########
    ########
     ######
      ####
       ##
    '''
    n = 4
    space = ' '
    pound = '#'
    rangeItem = list(range(1, n + 1))

    for i in rangeItem + rangeItem[::-1]:
        print((space * (n - i)) + (pound * i * 2) + (space * (n - i)))


if __name__ == '__main__':
    main()
