#!/usr/local/bin/python
# Code Fights Range Bit Count (Core) Problem


def rangeBitCount(a, b):
    return (''.join([bin(n) for n in range(a, b + 1)])).count('1')


def main():
    tests = [
        [2, 7, 11],
        [0, 1, 1],
        [1, 10, 17],
        [8, 9, 3],
        [9, 10, 4]
    ]

    for t in tests:
        res = rangeBitCount(t[0], t[1])
        if t[2] == res:
            print("PASSED: rangeBitCount({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: rangeBitCount({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
