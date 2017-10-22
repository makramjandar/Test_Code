#!/usr/local/bin/python
# Code Fights Are Equally Strong Problem


def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    s = {yourLeft, yourRight, friendsLeft, friendsRight}
    return (
        len(s) <= 2 and
        max(yourLeft, yourRight) == max(friendsLeft, friendsRight)
    )


def main():
    tests = [
        [10, 15, 15, 10, True],
        [15, 10, 15, 10, True],
        [15, 10, 15, 9, False],
        [10, 5, 5, 10, True],
        [10, 15, 5, 20, False],
        [10, 20, 10, 20, True],
        [5, 20, 20, 5, True],
        [20, 15, 5, 20, False],
        [5, 10, 5, 10, True],
        [1, 10, 10, 0, False],
        [5, 5, 10, 10, False],
        [10, 5, 10, 6, False],
        [1, 1, 1, 1, True]
    ]

    for t in tests:
        res = areEquallyStrong(t[0], t[1], t[2], t[3])
        if t[4] == res:
            print("PASSED: areEquallyStrong({}, {}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], t[3], res))
        else:
            print("FAILED: areEquallyStrong({}, {}, {}, {}) returned {}, should have returned {}"
                  .format(t[0], t[1], t[2], t[3], res, t[4]))


if __name__ == '__main__':
    main()
