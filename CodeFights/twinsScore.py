#!/usr/local/bin/python
# Code Fights Twins Score Problem


def twinsScore(b, m):
    return [sum(item) for item in zip(b, m)]


def main():
    tests = [
        [[22, 13, 45, 32], [28, 41, 13, 32], [50, 54, 58, 64]],
        [[0, 0, 0], [100, 100, 100], [100, 100, 100]],
        [[42], [42], [84]],
        [[46, 22, 2, 83, 15, 46, 98], [28, 33, 91, 71, 77, 35, 5],
            [74, 55, 93, 154, 92, 81, 103]],
        [[73, 5, 69, 88, 53, 8, 25, 52, 18, 61],
         [97, 61, 69, 10, 11, 13, 72, 3, 57, 47],
         [170, 66, 138, 98, 64, 21, 97, 55, 75, 108]]
    ]

    for t in tests:
        res = twinsScore(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: twinsScore({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: twinsScore({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
