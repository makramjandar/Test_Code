#!/usr/local/bin/python
# Code Fights Array Change Problem


def arrayChange(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        diff = inputArray[i] - inputArray[i - 1]
        if diff <= 0:
            inputArray[i] += abs(diff) + 1
            count += abs(diff) + 1
    return count


def main():
    tests = [
        [[1, 1, 1], 3]
    ]

    for t in tests:
        res = arrayChange(t[0])
        if t[1] == res:
            print("PASSED: arrayChange({}) returned {}".format(t[0], res))
        else:
            print("FAILED: arrayChange({}) returned {}, should have returned \
                {}".format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
