#!/usr/local/bin/python
# Code Fights Extract Each Kth Problem


def extractEachKth(inputArray, k):
    return [e for i, e in enumerate(inputArray) if (i + 1) % k != 0]


def main():
    tests = [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [1, 2, 4, 5, 7, 8, 10]],
        [[1, 1, 1, 1, 1], 1, []],
        [[1, 2, 1, 2, 1, 2, 1, 2], 2, [1, 1, 1, 1]]
    ]

    for t in tests:
        res = extractEachKth(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: extractEachKth({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: extractEachKth({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
