#!/usr/local/bin/python
# Code Fights Phone Call Problem


def phoneCall(min1, min2_10, min11, s):
    money_left = s
    talking = 0
    while money_left > 0:
        if talking < 1:
            if money_left - min1 < 0:
                return talking
            else:
                money_left -= min1
                talking += 1
        elif 1 <= talking < 10:
            if money_left - min2_10 < 0:
                return talking
            else:
                money_left -= min2_10
                talking += 1
        else:
            if money_left - min11 < 0:
                return talking
            else:
                money_left -= min11
                talking += 1
    return talking


def main():
    tests = [
        [3, 1, 2, 20, 14],
        [2, 2, 1, 2, 1],
        [10, 1, 2, 22, 11],
        [2, 2, 1, 24, 14],
        [1, 2, 1, 6, 3]
    ]

    for t in tests:
        res = phoneCall(t[0], t[1], t[2], t[3])
        if t[4] == res:
            print("PASSED: phoneCall({}, {}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], t[3], res))
        else:
            print("FAILED: phoneCall({}, {}, {}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], t[2], t[3], res, t[4]))


if __name__ == '__main__':
    main()
