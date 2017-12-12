#!/usr/local/bin/python
# Code Fights Array Packing (Core) Problem


def arrayPacking(a):
    return sum([n << 8*i for i, n in enumerate(a)])


def main():
    tests = [
        [[24, 85, 0], 21784],
        [[23, 45, 39], 2567447]
    ]

    for t in tests:
        res = arrayPacking(t[0])
        if t[1] == res:
            print("PASSED: arrayPacking({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: arrayPacking({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
