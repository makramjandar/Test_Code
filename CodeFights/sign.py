#!/usr/local/bin/python
# Code Fights Sign Problem


class Functions(object):
    def sign(x):
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1


def sign(x):
    return Functions.sign(x)


def main():
    tests = [
        [-34, -1],
        [42, 1],
        [0, 0]
    ]

    for t in tests:
        res = sign(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: sign({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: sign({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
