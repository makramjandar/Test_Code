#!/usr/local/bin/python
# Code Fights Calkin Wilf Problem


def calkinWilfSequence(number):
    def fractions():
        cur = (1, 1)
        while True:
            yield list(cur)
            cur = (cur[1], (2 * int(cur[0] / cur[1]) + 1) * cur[1] -
                   cur[0])

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


def main():
    tests = [
        [[1, 3], 3],
        [[1, 1], 0],
        [[3, 1], 6],
        [[14, 3], 110],
        [[7, 13], 129]
    ]

    for t in tests:
        res = calkinWilfSequence(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: calkinWilfSequence({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: calkinWilfSequence({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
