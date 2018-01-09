#!/usr/local/bin/python
# Code Fights Math Practice Problem

from functools import reduce


def mathPractice(numbers):
    return reduce(lambda acc, x: (acc + x[1] if x[0] % 2 else acc * x[1]),
                  enumerate(numbers), 1)


def main():
    tests = [
        [[1, 2, 3, 4, 5, 6], 71],
        [[8, 9], 17],
        [[0, 8, 15], 120],
        [[3, 18, 5, 17, 7, 12, 3, 14], 2612],
        [[9, 19, 2, 2, 7, 3, 0, 0, 6, 11, 14, 18, 11, 7, 9, 6, 8, 4, 13, 11],
         1778151]
    ]

    for t in tests:
        res = mathPractice(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: mathPractice({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: mathPractice({}) returned {}, answer: {}")
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
