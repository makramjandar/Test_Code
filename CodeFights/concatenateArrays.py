#!/usr/local/bin/python
# Code Fights Concatenate Arrays Problem


def concatenateArrays(a, b):
    return a + b


def main():
    tests = [
        [[2, 2, 1], [10, 11], [2, 2, 1, 10, 11]],
        [[1, 2], [3, 1, 2], [1, 2, 3, 1, 2]],
        [[1], [], [1]],
        [
            [2, 10, 3, 9, 5, 11, 11],
            [4, 8, 1, 13, 3, 1, 14],
            [2, 10, 3, 9, 5, 11, 11, 4, 8, 1, 13, 3, 1, 14]
        ],
        [
            [9, 6, 6, 9, 8, 14],
            [3, 2, 2, 5, 3, 11, 12, 9, 7, 7],
            [9, 6, 6, 9, 8, 14, 3, 2, 2, 5, 3, 11, 12, 9, 7, 7]
        ]
    ]

    for t in tests:
        res = concatenateArrays(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: concatenateArrays({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: concatenateArrays({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
