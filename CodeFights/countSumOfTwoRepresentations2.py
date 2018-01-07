#!/usr/local/bin/python
# Code Fights Count of Two Representations 2 Problem


def countSumOfTwoRepresentations2(n, l, r):
    return sum(1 for x in range(l, r + 1) if x <= n - x <= r)


def main():
    tests = [
        [6, 2, 4, 2],
        [6, 3, 3, 1],
        [10, 9, 11, 0],
        [24, 8, 16, 5],
        [24, 12, 12, 1],
        [93, 24, 58, 12]
    ]

    for t in tests:
        res = countSumOfTwoRepresentations2(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: countSumOfTwoRepresentations2({}, {}, {}) returned"
                  " {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: countSumOfTwoRepresentations2({}, {}, {}) returned"
                   " {}, answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
