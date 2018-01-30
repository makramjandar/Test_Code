#!/usr/local/bin/python
# Code Fights Is Digit Problem

import re


def isDigit(symbol):
    return bool(re.search(r'\d', symbol))


def main():
    tests = [
        ["0", True],
        ["-", False],
        ["o", False],
        ["1", True],
        ["2", True],
        ["!", False],
        ["@", False],
        ["+", False],
        ["6", True],
        ["(", False],
        [")", False]
    ]

    for t in tests:
        res = isDigit(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isDigit({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isDigit({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
