#!/usr/local/bin/python
# Code Fights Replace Middle Problem


def replaceMiddle(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr
    else:
        mid = arr[n // 2 - 1] + arr[n // 2]
        arr[n // 2 - 1: n // 2 + 1] = [mid]
        return arr


def main():
    tests = [
        [[7, 2, 2, 5, 10, 7], [7, 2, 7, 10, 7]],
        [[-5, -5, 10], [-5, -5, 10]],
        [
            [45, 23, 12, 33, 12, 453, -234, -45],
            [45, 23, 12, 45, 453, -234, -45]
        ],
        [[2, 8], [10]],
        [
            [-12, 34, 40, -5, -12, 4, 0, 0, -12],
            [-12, 34, 40, -5, -12, 4, 0, 0, -12]
        ],
        [[9, 0, 15, 9], [9, 15, 9]],
        [[-6, 6, -6], [-6, 6, -6]],
        [[26, 26, -17], [26, 26, -17]],
        [[-7, 5, 5, 10], [-7, 10, 10]]
    ]

    for t in tests:
        res = replaceMiddle(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: replaceMiddle({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: replaceMiddle({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
