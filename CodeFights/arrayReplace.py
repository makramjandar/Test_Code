#!/usr/local/bin/python
# Code Fights Add Border Problem


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [x if x != elemToReplace else substitutionElem for x in inputArray]


def main():
    tests = [
        [[1, 2, 1], 1, 3, [3, 2, 3]],
        [[1, 2, 3, 4, 5], 3, 0, [1, 2, 0, 4, 5]],
        [[1, 1, 1], 1, 10, [10, 10, 10]]
    ]

    for t in tests:
        res = arrayReplace(t[0], t[1], t[2])
        if t[3] == res:
            print("PASSED: arrayReplace({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print("FAILED: arrayReplace({}, {}, {}) returned {}, should have returned {}"
                  .format(t[0], t[1], t[2], res, t[3]))


if __name__ == '__main__':
    main()
