#!/usr/local/bin/python
# Code Fights Rounders Problem


def rounders(value):
    return value


def main():
    tests = [
        [15, 20],
        [1234, 1000],
        [1445, 2000],
        [14, 10],
        [10, 10],
        [99, 100]
    ]

    for t in tests:
        res = rounders(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: rounders({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: rounders({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
