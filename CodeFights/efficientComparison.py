#!/usr/local/bin/python
# Code Fights Efficient Comparison Problem

import time


def main():
    x, y, L, R = 9, 9, 1, 10000
    print("Procedure 1")
    t1 = time.clock()
    procedure1(x, y, L, R)
    print(time.clock() - t1)

    print("Procedure 2")
    t2 = time.clock()
    procedure2(x, y, L, R)
    print(time.clock() - t2)

    print("Procedure 3")
    t3 = time.clock()
    procedure3(x, y, L, R)
    print(time.clock() - t3)


def procedure1(x, y, L, R):
    return L < x**y <= R


def procedure2(x, y, L, R):
    return x**y > L and x**y <= R


def procedure3(x, y, L, R):
    return x**y in range(L + 1, R + 1)


if __name__ == '__main__':
    main()
