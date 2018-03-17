#!/usr/local/bin/python
# Code Fights Digit Degree Problem


def digitDegree(n):
    degree = 0
    if n < 10:
        return 0
    while n > 0:
        dig = n % 10
        n = n // 10
        if dig > 0:
            degree += 1
    return degree


def main():
    tests = [
        [5, 0],
        [100, 1],
        [91, 2],
        [99, 2]
    ]

    for t in tests:
        res = digitDegree(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: digitDegree({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: digitDegree({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
