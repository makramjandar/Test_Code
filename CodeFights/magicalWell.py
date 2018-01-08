#!/usr/local/bin/python
# Code Fights Magical Well Problem


def magicalWell(a, b, n):
    return sum([x * y for (x, y) in zip(range(a, a + n), range(b, b + n))])


def main():
    tests = [
        [1, 2, 2, 8],
        [1, 1, 1, 1],
        [6, 5, 3, 128]
    ]

    for t in tests:
        res = magicalWell(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: magicalWell({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: magicalWell({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
