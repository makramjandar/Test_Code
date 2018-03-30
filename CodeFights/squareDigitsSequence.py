#!/usr/local/bin/python
# Code Fights Square Digits Sequence Problem


def squareDigitsSequence(a0):
    squares = [a0]
    nxt = a0
    while True:
        new = sum([int(d)**2 for d in str(nxt)])
        squares.append(new)
        if new in squares[:-1]:
            break
        nxt = new

    return len(squares)


def main():
    tests = [
        [16, 9],
        [103, 4],
        [1, 2]
    ]

    for t in tests:
        res = squareDigitsSequence(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: squareDigitsSequence({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: squareDigitsSequence({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
