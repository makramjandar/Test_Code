#!/usr/local/bin/python
# Code Fights First Digit Problem

import re


def firstDigit(inputString):
    match = re.search(r'\d', inputString)
    return match.group(0)


def main():
    tests = [
        ["var_1__Int", "1"],
        ["q2q-q", "2"],
        ["0ss", "0"]
    ]

    for t in tests:
        res = firstDigit(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: firstDigit({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: firstDigit({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
