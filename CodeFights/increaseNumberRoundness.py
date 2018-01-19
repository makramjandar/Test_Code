#!/usr/local/bin/python
# Code Fights Increase Number Roundness Problem

import re


def increaseNumberRoundness(n):
    pattern = re.compile(r'0+[1-9]+')
    return bool(re.search(pattern, str(n)))


def main():
    tests = [
        [902200100, True],
        [11000, False],
        [99080, True],
        [1022220, True],
        [106611, True],
        [234230, False],
        [888, False],
        [100, False],
        [1000000000, False],
        [103456789, True]
    ]

    for t in tests:
        res = increaseNumberRoundness(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: increaseNumberRoundness({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: increaseNumberRoundness({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
