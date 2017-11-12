#!/usr/local/bin/python
# Code Fights Late Ride Problem


def lateRide(n):
    h, m = divmod(n, 60)
    return sum(map(int, str(h) + str(m)))


def main():
    tests = [
        [240, 4],
        [808, 14],
        [1439, 19],
        [0, 0],
        [23, 5],
        [8, 8]
    ]

    for t in tests:
        res = lateRide(t[0])
        if t[1] == res:
            print("PASSED: lateRide({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: lateRide({}) returned {}, answer: {}"
                  .format(t[0], res, t[2]))


if __name__ == '__main__':
    main()
