#!/usr/local/bin/python
# Code Fights Swap Adjacent Bits (Core) Problem


def swapAdjacentBits(n):
    # even = n & 0xaaaaaaaa  # mask to keep only even bits with 10 16x
    # odd = n & 0x55555555  # mask to keep only odd bits with 01 16x
    # even = even >> 1  # left shift even bits
    # odd = odd << 1  # right shift odd bits
    # return even | odd  # combine
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


def main():
    tests = [
        [13, 14],
        [74, 133],
        [1073741823, 1073741823],
        [0, 0],
        [1, 2],
        [83748, 166680]
    ]

    for t in tests:
        res = swapAdjacentBits(t[0])
        # print("Input: {}\nBits: {}".format(t[0], bin(t[0])[2:]))
        # print("Answer: {}\nBits: {}".format(t[1], bin(t[1])[2:]))
        # print("Output: {}\nBits: {}".format(res, bin(res)[2:]))
        if t[1] == res:
            print("PASSED: swapAdjacentBits({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: swapAdjacentBits({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
