#!/usr/local/bin/python
# Code Fights Is Beautiful String Problem

import string


def isBeautifulString(inputString):
    keys = string.ascii_lowercase
    for i in range(1, len(keys)):
        if inputString.count(keys[i]) > inputString.count(keys[i - 1]):
            return False

    return True


def main():
    tests = [
        ["bbbaacdafe", True],
        ["aabbb", False],
        ["bbc", False],
        ["bbbaa", False],
        ["abcdefghijklmnopqrstuvwxyzz", False],
        ["abcdefghijklmnopqrstuvwxyz", True],
        ["abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm", True],
        ["fyudhrygiuhdfeis", False],
        ["zaa", False],
        ["zyy", False]
    ]

    for t in tests:
        res = isBeautifulString(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isBeautifulString({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: isBeautifulString({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
