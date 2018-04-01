#!/usr/local/bin/python
# Code Fights Pages Numbering With Ink Problem

import math


def pagesNumberingWithInk(current, numberOfDigits):
    num = current
    digits = (int(math.log(num, 10)) + 1)
    available = numberOfDigits - digits
    while available >= digits:
        digits = int(math.log(num + 1, 10)) + 1
        if digits <= available:
            num += 1
            available -= digits
        else:
            return num

    return num


def main():
    tests = [
        [1, 5, 5],
        [21, 5, 22],
        [8, 4, 10],
        [21, 6, 23],
        [76, 250, 166],
        [80, 1000, 419]
    ]

    for t in tests:
        res = pagesNumberingWithInk(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: pagesNumberingWithInk({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: pagesNumberingWithInk({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
