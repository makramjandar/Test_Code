#!/usr/local/bin/python
# Code Fights Cyclic Name Problem

from itertools import cycle


def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)


def main():
    tests = [
        ["nicecoder", 15, "nicecoderniceco"],
        ["codefights", 50, "codefightscodefightscodefightscodefightscode"
            "fights"],
        ["test", 4, "test"],
        ["q", 8, "qqqqqqqq"],
        ["ninja", 15, "ninjaninjaninja"]
    ]

    for t in tests:
        res = cyclicName(t[0], t[1])
        if t[2] == res:
            print("PASSED: cyclicName({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: cyclicName({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
