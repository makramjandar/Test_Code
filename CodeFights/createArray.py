#!/usr/local/bin/python
# Code Fights Create Array Problem


def createArray(size):
    return [1] * size


def main():
    tests = [
        [4, [1, 1, 1, 1]],
        [2, [1, 1]],
        [1, [1]],
        [5, [1, 1, 1, 1, 1]]
    ]

    for t in tests:
        res = createArray(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: createArray({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: createArray({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
