#!/usr/local/bin/python
# Code Fights Make Array Consecutive 2 Problem


def makeArrayConsecutive2(statues):
    return (len(range(min(statues), max(statues) + 1)) - len(statues))


def main():
    tests = [
        [[6, 2, 3, 8], 3],
        [[0, 3], 2],
        [[5, 4, 6], 0],
        [[6, 3], 2],
        [[1], 0]
    ]

    for t in tests:
        res = makeArrayConsecutive2(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: makeArrayConsecutive2({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: makeArrayConsecutive2({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
