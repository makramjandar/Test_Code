#!/usr/local/bin/python
# Code Fights Fibonacci List Problem

from functools import reduce


def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x, n: x + [sum(x[-2:])],
                                    range(n - 2), [0, 1])]


def main():
    tests = [
        [
            6,
            [[],
             [0],
             [0],
             [0, 0],
             [0, 0, 0],
             [0, 0, 0, 0, 0]]
        ],
        [
            2,
            [[],
             [0]]
        ],
        [
            3,
            [[],
             [0],
             [0]]
        ],
        [
            8,
            [[],
             [0],
             [0],
             [0, 0],
             [0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ],
        [
            5,
            [[],
             [0],
             [0],
             [0, 0],
             [0, 0, 0]]
        ]
    ]

    for t in tests:
        res = fibonacciList(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: fibonacciList({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: fibonacciList({}) returned {}, answer: {}")
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
