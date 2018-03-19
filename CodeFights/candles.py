#!/usr/local/bin/python
# Code Fights Candles Problem


def candles(candlesNumber, makeNew):
    burned = candlesNumber
    stubs = candlesNumber
    while stubs >= makeNew:
        burnable = stubs // makeNew
        burned += burnable
        stubs -= burnable * makeNew
        stubs += burnable

    return burned


def main():
    tests = [
        [5, 2, 9],
        [1, 2, 1],
        [3, 3, 4],
        [11, 3, 16]
    ]

    for t in tests:
        res = candles(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: candles({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: candles({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
