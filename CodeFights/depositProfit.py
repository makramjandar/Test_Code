#!/usr/local/bin/python
# Code Fights Deposit Profit Problem


def depositProfit(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        deposit *= 1 + rate / 100
        years += 1

    return years


def main():
    tests = [
        [100, 20, 170, 3],
        [100, 1, 101, 1],
        [1, 100, 64, 6]
    ]

    for t in tests:
        res = depositProfit(t[0], t[1], t[2])
        if t[3] == res:
            print("PASSED: depositProfit({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print("FAILED: depositProfit({}, {}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], t[2], res, t[3]))


if __name__ == '__main__':
    main()
