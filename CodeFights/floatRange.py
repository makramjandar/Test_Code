#!/usr/local/bin/python
# Code Fights Float Range Problem

from itertools import count, takewhile


def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)


def main():
    tests = [
        [-0.9, 0.45, 0.2, [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]],
        [1.5, 1.5, 10, []],
        [1, 2, 1.5, [1]],
        [-21.11, 21.11, 1.11,
            [-21.11, -20, -18.89, -17.78, -16.67, -15.56, -14.45, -13.34,
             -12.23, -11.12, -10.01, -8.9, -7.79, -6.68, -5.57, -4.46, -3.35,
             -2.24, -1.13, -0.02, 1.09, 2.2, 3.31, 4.42, 5.53, 6.64, 7.75,
             8.86, 9.97, 11.08, 12.19, 13.3, 14.41, 15.52, 16.63, 17.74, 18.85,
             19.96, 21.07]],
        [0, 1, 0.5,
            [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
             0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]]
    ]

    for t in tests:
        res = floatRange(t[0], t[1], t[2])
        if t[3] == res:
            print("PASSED: floatRange({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: floatRange({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, t[3]))


if __name__ == '__main__':
    main()
