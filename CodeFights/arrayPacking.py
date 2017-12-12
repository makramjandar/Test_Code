#!/usr/local/bin/python
# Code Fights Are Equally Strong Problem


def arrayPacking():
    pass


def main():
    tests = [
        [],
        []
    ]

    for t in tests:
        res = arrayPacking(t[0])
        if t[1] == res:
            print("PASSED: arrayPacking({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: arrayPacking({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
