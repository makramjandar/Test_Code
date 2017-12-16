#!/usr/local/bin/python
# Code Second Right-most Zero Bit (Core) Problem


def secondRightmostZeroBit(n):
    # print('Number: {}\nBinary: {}'.format(n, bin(n)))
    # Solution:
    # return (((((n + 1) | n) + 1) | n) - n)
    return [2**i for i in range(len(bin(n)[2:])) if (n >> i) % 2 == 0][1]


def main():
    tests = [
        [37, 8],
        [1073741824, 2],
        [83748, 2],
        [4, 2],
        [728782938, 4]
    ]

    for t in tests:
        res = secondRightmostZeroBit(t[0])
        if t[1] == res:
            print("PASSED: secondRightmostZeroBit({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: secondRightmostZeroBit({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
