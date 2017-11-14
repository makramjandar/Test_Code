#!/usr/local/bin/python
# Code Fights Absolute Values Sum Minimization Problem


def absoluteValuesSumMinimization(a):
    mid = len(a) // 2
    return a[mid] if len(a) % 2 == 1 else min(a[mid], a[mid - 1])


def main():
    tests = [
        [[2, 4, 7], 4],
        [[1, 1, 3, 4], 1],
        [[23], 23],
        [
            [
                -10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4,
                -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                45, 46, 47, 48, 49, 50
            ],
            15
        ],
        [[-4, -1], -4],
        [[0, 7, 9], 7],
        [
            [
                -1000000, -10000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100,
                1000, 10000, 100000, 1000000
            ],
            0
        ]
    ]

    for t in tests:
        res = absoluteValuesSumMinimization(t[0])
        if t[1] == res:
            print("PASSED: absoluteValuesSumMinimization({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: absoluteValuesSumMinimization({}) returned {}, "
                  "answer: {}".format(t[0], res, t[1]))


if __name__ == '__main__':
    main()


absoluteValuesSumMinimization
