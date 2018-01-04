#!/usr/local/bin/python
# Code Fights Bishop and Pawn Problem


def bishopAndPawn(bishop, pawn):
    epsilon = 0.001
    dist = ((ord(bishop[0]) - ord(pawn[0]))**2 +
            (int(bishop[1]) - int(pawn[1]))**2)**(0.5)
    dist = dist / (2**0.5)  # distance is a multiple of sqrt(2)
    return (round(dist) - dist < epsilon and bishop[0] != pawn[0] and
            bishop[1] != pawn[1])


def main():
    tests = [
        ["a1", "c3", True],
        ["h1", "h3", False],
        ["a5", "c3", True],
        ["g1", "f3", False],
        ["e7", "d6", True],
        ["e7", "a3", True],
        ["e3", "a7", True],
        ["a1", "h8", True],
        ["a1", "h7", False],
        ["h1", "a8", True]
    ]

    for t in tests:
        res = bishopAndPawn(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: bishopAndPawn({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: bishopAndPawn({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
