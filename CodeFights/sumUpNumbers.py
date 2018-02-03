#!/usr/local/bin/python
# Code Fights Sum Up Numbers Problem

import re


def sumUpNumbers(inputString):
    return sum([int(n) for n in re.findall(r'\d+', inputString)])


def main():
    tests = [
        ["2 apples, 12 oranges", 14],
        ["123450", 123450],
        ["Your payment method is invalid", 0]
    ]

    for t in tests:
        res = sumUpNumbers(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: sumUpNumbers({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: sumUpNumbers({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
