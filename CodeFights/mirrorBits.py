#!/usr/local/bin/python
# Code Fights Mirror Bits (Core) Problem


def mirrorBits(a):
    return int(bin(a)[::-1][:-2], 2)


def main():
    tests = [
        [97, 67],
        [8, 1]
    ]

    for t in tests:
        res = mirrorBits(t[0])
        if t[1] == res:
            print("PASSED: mirrorBits({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: mirrorBits({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
