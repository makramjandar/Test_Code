#!/usr/local/bin/python
# Code Fights Equal Pair of Bits (Core) Problem


def equalPairOfBits(n, m):
    return ~(n ^ m) & -~(n ^ m)


def main():
    tests = [
        [10, 11, 2],
        [0, 0, 1],
        [28, 27, 8],
        [895, 928, 32],
        [1073741824, 1006895103, 262144]
    ]

    for t in tests:
        res = equalPairOfBits(t[0], t[1])
        if t[2] == res:
            print("PASSED: equalPairOfBits({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: equalPairOfBits({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
