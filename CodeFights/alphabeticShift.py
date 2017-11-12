#!/usr/local/bin/python
# Code Fights Alternating Sums Problem


def alphabeticShift(inputString):
    test = [chr((ord(c) - 96) % 26 + 97) for c in inputString]
    return ''.join(test)


def main():
    tests = [
        ["crazy", "dsbaz"],
        ["z", "a"]
    ]

    for t in tests:
        res = alphabeticShift(t[0])
        if t[1] == res:
            print("PASSED: alphabeticShift({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: alphabeticShift({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
