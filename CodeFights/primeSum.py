#!/usr/local/bin/python
# Code Fights Prime Sum Problem


def primeSum(a, b):
    return sum(filter(lambda p: p > 1 and all(p % n for n in
               range(2, int(p**0.5) + 1)), range(a, b + 1)))


def main():
    tests = [
        [10, 20, 60],
        [1, 7, 17],
        [5, 10, 12],
        [24, 28, 0],
        [13, 13, 13]
    ]

    for t in tests:
        res = primeSum(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: primeSum({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: primeSum({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
