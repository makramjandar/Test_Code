#!/usr/local/bin/python
# Code Fights Alphabetic Shift Problem

from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda i_x: i_x[1].rotate(-i_x[0]), enumerate(res)), 0)
    return [list(d) for d in res]


def main():
    tests = [
        [
            [1, 2, 3, 4, 5],
            [
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 1],
                [3, 4, 5, 1, 2],
                [4, 5, 1, 2, 3],
                [5, 1, 2, 3, 4]
            ]
        ],
        [[5], [[5]]],
        [
            [2, 2, 2, 2],
            [
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2]
            ]
        ],
        [
            [9, 8, 7, 5, 4],
            [
                [9, 8, 7, 5, 4],
                [8, 7, 5, 4, 9],
                [7, 5, 4, 9, 8],
                [5, 4, 9, 8, 7],
                [4, 9, 8, 7, 5]
            ]
        ],
        [
            [1, 5, 1, 5, 1, 4],
            [
                [1, 5, 1, 5, 1, 4],
                [5, 1, 5, 1, 4, 1],
                [1, 5, 1, 4, 1, 5],
                [5, 1, 4, 1, 5, 1],
                [1, 4, 1, 5, 1, 5],
                [4, 1, 5, 1, 5, 1]
            ]
        ]
    ]

    for t in tests:
        res = doodledPassword(t[0])
        if t[1] == res:
            print("PASSED: doodledPassword({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: doodledPassword({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
