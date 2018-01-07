#!/usr/local/bin/python
# Code Fights Pref Sum Problem

from itertools import accumulate


def prefSum(a):
    return list(accumulate(a))


def main():
    tests = [
        [[1, 2, 3], [1, 3, 6]],
        [[1, 2, 3, -6], [1, 3, 6, 0]],
        [[0, 0, 0], [0, 0, 0]]
    ]

    for t in tests:
        res = prefSum(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: prefSum({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: prefSum({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
