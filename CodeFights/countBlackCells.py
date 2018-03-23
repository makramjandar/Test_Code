#!/usr/local/bin/python
# Code Fights Count Black Cells Problem

from fractions import gcd


def countBlackCells(m, n):
    # Manhattan distance plus lattice points less 2 end points
    return (m + n) + gcd(n, m) - 2


def main():
    tests = [
        [3, 4, 6],
        [3, 3, 7],
        [2, 5, 6],
        [1, 1, 1],
        [1, 2, 2],
        [1, 3, 3],
        [1, 239, 239],
        [33, 44, 86],
        [16, 8, 30],
        [66666, 88888, 177774]
    ]

    for t in tests:
        res = countBlackCells(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: countBlackCells({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: countBlackCells({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
