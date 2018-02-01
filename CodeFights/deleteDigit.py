#!/usr/local/bin/python
# Code Fights Delete Digit Problem


def deleteDigit(n):
    s = str(n)
    return max(int(''.join(s[:i] + s[i + 1:])) for i in range(len(s)))
    # idxs = [i for i in range(len(s) - 1) if int(s[i]) < int(s[i + 1])]
    # if idxs:
    #     return int(s[:idxs[0]] + s[idxs[0] + 1:])
    # else:
    #     return int(s[:-1])


def main():
    tests = [
        [152, 52],
        [1001, 101],
        [10, 1],
        [222219, 22229]
    ]

    for t in tests:
        res = deleteDigit(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: deleteDigit({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: deleteDigit({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
