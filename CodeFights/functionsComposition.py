#!/usr/local/bin/python
# Code Fights Functions Composition Problem

from functools import reduce
import math


def compose(functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)


def main():
    tests = [
        [["abs", "math.sin", "lambda x: 3 * x / 2"], math.pi, 1],
        [["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"],
         1, math.sin(math.cos((1**2) * 2))],
        [["lambda z: z", "lambda z: 1.0 * z / 13"], -1000, (-1000 / 13) * 1.0],
        [["float"], 1000, 1000],
        [["abs"], -20, 20]
    ]

    for t in tests:
        res = functionsComposition(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: functionsComposition({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: functionsComposition({}, {}) returned {},"
                  "answer: {}".format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
