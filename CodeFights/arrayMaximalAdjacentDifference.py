#!/usr/local/bin/python
# Code Fights Array Maximal Adjacent Difference Problem


def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i] - inputArray[i - 1])
                for i in range(1, len(inputArray))])


def main():
    tests = [
        [[2, 4, 1, 0], 3],
        [[1, 1, 1, 1], 0],
        [[-1, 4, 10, 3, -2], 7]
    ]

    for t in tests:
        res = arrayMaximalAdjacentDifference(t[0])
        if t[1] == res:
            print("PASSED: arrayMaximalAdjacentDifference({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: arrayMaximalAdjacentDifference({}) returned {}, should have returned {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
