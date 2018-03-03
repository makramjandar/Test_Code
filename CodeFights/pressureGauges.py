#!/usr/local/bin/python
# Code Fights Pressure Gauges Problem


def pressureGauges(morning, evening):
    return [list(map(min, zip(morning, evening))),
            list(map(max, zip(morning, evening)))]


def main():
    tests = [
        [[3, 5, 2, 6], [1, 6, 6, 6], [[1, 5, 2, 6], [3, 6, 6, 6]]],
        [[0, 12, 478, 23, 1000], [48, 23, 56, 23, 88],
         [[0, 12, 56, 23, 88], [48, 23, 478, 23, 1000]]],
        [[8], [1], [[1], [8]]],
        [[129, 553, 585], [852, 601, 997], [[129, 553, 585], [852, 601, 997]]],
        [[734, 483, 87, 499, 931, 657, 833],
         [316, 511, 592, 355, 819, 621, 419],
         [[316, 483, 87, 355, 819, 621, 419],
          [734, 511, 592, 499, 931, 657, 833]]]
    ]

    for t in tests:
        res = pressureGauges(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: pressureGauges({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: pressureGauges({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
