#!/usr/local/bin/python
# Code Fights Is Smooth Problem


def isSmooth(arr):
    elems = len(arr)
    middle = (arr[elems // 2] if elems % 2 == 1
              else arr[elems // 2 - 1] + arr[elems // 2])
    return middle == arr[0] == arr[-1]


def main():
    tests = [
        [[7, 2, 2, 5, 10, 7], True],
        [[-5, -5, 10], False],
        [[4, 2], False],
        [[45, 23, 12, 33, 12, 453, -234, -45], False],
        [[-12, 34, 40, -5, -12, 4, 0, 0, -12], True],
        [[9, 0, 15, 9], False],
        [[-6, 6, -6], False],
        [[26, 26, -17], False],
        [[-7, 5, 5, 10], False],
        [[3, 4, 5], False],
        [[-5, 3, -1, 9], False]
    ]

    for t in tests:
        res = isSmooth(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isSmooth({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isSmooth({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
