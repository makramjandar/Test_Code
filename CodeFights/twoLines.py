#!/usr/local/bin/python
# Code Fights Two Lines Problem

from functools import partial


def line_y(m, b, x):
    return m * x + b


def twoLines(line1, line2, l, r):
    line1_y = partial(line_y, *line1)
    line2_y = partial(line_y, *line2)
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"


def main():
    tests = [
        [[1, 2], [2, 1], 0, 2, "any"],
        [[1, 2], [2, 1], -1, 2, "first"],
        [[1, 2], [2, 1], 0, 3, "second"],
        [[1, 2], [1, 0], -1000, 1000, "first"],
        [[1, 0], [-1, 0], -239, 239, "any"],
        [[1, 0], [-1, 0], -999, 998, "second"]
    ]

    for t in tests:
        res = twoLines(t[0], t[1], t[2], t[3])
        ans = t[4]
        if ans == res:
            print("PASSED: twoLines({}, {}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], t[3], res))
        else:
            print(("FAILED: twoLines({}, {}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], t[3], res, ans))


if __name__ == '__main__':
    main()
