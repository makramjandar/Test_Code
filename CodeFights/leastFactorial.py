#!/usr/local/bin/python
# Code Fights Least Factorial (Core) Problem


def leastFactorial(n):
    def factGen():
        m, res = 1, 1
        while True:
            res *= m
            yield res
            m += 1

    for f in factGen():
        if f >= n:
            return f


def main():
    tests = [
        [17, 24],
        [1, 1],
        [5, 6]
    ]

    for t in tests:
        res = leastFactorial(t[0])
        if t[1] == res:
            print("PASSED: leastFactorial({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: leastFactorial({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
