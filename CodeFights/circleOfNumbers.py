#!/usr/local/bin/python
# Code Fights Circle of Numbers Problem


def circleOfNumbers(n, firstNumber):
    mid = n / 2
    return (mid + firstNumber if firstNumber < mid else firstNumber - mid)


def main():
    tests = [
        [10, 2, 7],
        [10, 7, 2],
        [4, 1, 3],
        [6, 3, 0]
    ]

    for t in tests:
        res = circleOfNumbers(t[0], t[1])
        if t[2] == res:
            print("PASSED: circleOfNumbers({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: circleOfNumbers({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
