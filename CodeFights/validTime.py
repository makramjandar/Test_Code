#!/usr/local/bin/python
# Code Fights Valid Time Problem


def validTime(time):
    h, m = tuple([int(d) for d in time.split(":")])
    return (0 <= h <= 23) and (0 <= m <= 59)


def main():
    tests = [
        ["13:58", True],
        ["25:51", False],
        ["02:76", False],
        ["24:00", False],
        ["0:00", True]
    ]

    for t in tests:
        res = validTime(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: validTime({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: validTime({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
