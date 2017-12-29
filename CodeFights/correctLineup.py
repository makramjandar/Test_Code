#!/usr/local/bin/python
# Code Fights Correct Lineup Problem


def correctLineup(athletes):
    return [a for t in zip(athletes[1::2], athletes[::2]) for a in t]


def main():
    tests = [
        [[1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]],
        [[13, 42], [42, 13]],
        [[2, 3, 1, 100, 99, 45, 22, 28], [3, 2, 100, 1, 45, 99, 28, 22]],
        [[85, 32, 45, 67, 32, 12, 45, 67], [32, 85, 67, 45, 12, 32, 67, 45]],
        [[60, 2, 24, 40], [2, 60, 40, 24]]
    ]

    for t in tests:
        res = correctLineup(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: correctLineup({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: correctLineup({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
