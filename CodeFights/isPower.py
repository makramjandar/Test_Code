#!/usr/local/bin/python
# Code Fights Is Power Problem


def isPower(n):
    if n == 1:
        return True
    for exp in range(2, 9):
        for base in range(2, n):
            tmp = base ** exp
            if tmp == n:
                return True
            elif tmp > n:
                break
    return False


def main():
    tests = [
        [125, True],
        [72, False],
        [100, True],
        [11, False],
        [324, True],
        [256, True],
        [119, False],
        [400, True],
        [350, False],
        [361, True]
    ]

    for t in tests:
        res = isPower(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isPower({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isPower({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
