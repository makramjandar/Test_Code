#!/usr/local/bin/python
# Code Fights Remove Array Part Problem


def removeArrayPart(inputArray, l, r):
    return inputArray[:l] + inputArray[r + 1:]


def main():
    tests = [
        [[2, 3, 2, 3, 4, 5], 2, 4, [2, 3, 5]],
        [[2, 4, 10, 1], 0, 2, [1]],
        [[5, 3, 2, 3, 4], 1, 1, [5, 2, 3, 4]]
    ]

    for t in tests:
        res = removeArrayPart(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: removeArrayPart({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: removeArrayPart({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
