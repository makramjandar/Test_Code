#!/usr/local/bin/python
# Code Fights Different Right-most Bit (Core) Problem


def differentRightmostBit(n, m):
    return (n ^ m) & -(n ^ m)


def main():
    tests = [
        [11, 13, 2],
        [7, 23, 16],
        [1, 0, 1],
        [64, 65, 1],
        [1073741823, 1071513599, 131072],
        [42, 22, 4]
    ]

    for t in tests:
        res = differentRightmostBit(t[0], t[1])
        if t[2] == res:
            print("PASSED: differentRightmostBit({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: differentRightmostBit({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
