#!/usr/local/bin/python
# Code Fights Circle of Numbers Problem


def circleOfNumbers(n, firstNumber):
    pass


def main():
    tests = [
        ["crazy", "dsbaz"],
        ["z", "a"]
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
