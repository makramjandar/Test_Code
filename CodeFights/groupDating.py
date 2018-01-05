#!/usr/local/bin/python
# Code Fights Group Dating Problem


def groupDating(male, female):
    return ([list(t) for t in zip(*filter(lambda x: x[0] != x[1],
            zip(male, female)))] if male != female else [[], []])


def main():
    tests = [
        [
            [5, 28, 14, 99, 17],
            [5, 14, 28, 99, 16],
            [[28, 14, 17], [14, 28, 16]]
        ],
        [
            [42],
            [64],
            [[42], [64]]
        ],
        [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [[], []]
        ],
        [
            [6, 23, 82],
            [82, 56, 92],
            [[6, 23, 82], [82, 56, 92]]
        ]
    ]

    for t in tests:
        res = groupDating(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: groupDating({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: groupDating({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
