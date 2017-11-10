#!/usr/local/bin/python
# Code Fights Add Border Problem


def evenDigitsOnly(n):
    return sum(map(lambda d: int(d) % 2, str(n))) == 0
    # Alternative solution
    # return all([int(i) % 2 == 0 for i in str(n)])


def main():
    tests = [
        [248622, True],
        [642386, False],
        [248842, True],
        [1, False],
        [8, True],
        [2462487, False],
        [468402800, True],
        [2468428, True],
        [5468428, False],
        [7468428, False]
    ]

    for t in tests:
        res = evenDigitsOnly(t[0])
        if t[1] == res:
            print("PASSED: evenDigitsOnly({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: evenDigitsOnly({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
