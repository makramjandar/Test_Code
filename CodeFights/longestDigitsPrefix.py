#!/usr/local/bin/python
# Code Fights Longest Digits Prefix Problem

import re


def longestDigitsPrefix(inputString):
    return re.findall(r'^\d*', inputString)[0]


def main():
    tests = [
        ["123aa1", "123"],
        ["0123456789", "0123456789"],
        ["  3) always check for whitespaces", ""],
        ["12abc34", "12"],
        ["the output is 42", ""]
    ]

    for t in tests:
        res = longestDigitsPrefix(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: longestDigitsPrefix({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: longestDigitsPrefix({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
