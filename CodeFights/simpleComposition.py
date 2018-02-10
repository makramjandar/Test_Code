#!/usr/local/bin/python
# Code Fights Simple Composition Problem

import math


def compose(f, g):
    return lambda x: f(g(x))


def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)


def main():
    tests = [
        ["math.log10", "abs", -100, 2],
        ["math.sin", "math.cos", 34.4, math.sin(math.cos(34.4))],
        ["int", "lambda x: 1.0 * x / 22", 1000, 45],
        ["math.exp", "lambda x: x ** 0", -1000, math.e],
        ["lambda z: z", "lambda y: y", 239, 239]
    ]

    for t in tests:
        res = simpleComposition(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: simpleComposition({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: simpleComposition({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
