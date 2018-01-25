#!/usr/local/bin/python
# Code Fights Try Functions Problem

import math


def tryFunctions(x, functions):
    return [eval(func)(x) for func in functions]


def main():
    tests = [
        [1, ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"],
         [0.84147, 0.5403, 2, 1]],
        [-20, ["abs"], [20]],
        [25.5, ["lambda x: int(x)", "int", "math.floor"], [25, 25, 25]],
        [3, ["math.factorial", "math.exp", "lambda x: 2 ** x"],
         [6, 20.0855369232, 8]],
        [-1000, ["lambda z: z", "lambda z: 1.0 * z / 13"],
         [-1000, -76.9230769231]]
    ]

    for t in tests:
        res = tryFunctions(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: tryFunctions({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: tryFunctions({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
