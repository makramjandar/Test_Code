#!/usr/local/bin/python
# Code Fights Lineup Problem


def lineUp(commands):
    aligned, tmp = 0, 0
    com_dict = {"L": 1, "A": 0, "R": -1}
    for c in commands:
        tmp += com_dict[c]
        if tmp % 2 == 0:
            aligned += 1
    return aligned


def main():
    tests = [
        ["LLARL", 3],
        ["RLR", 1],
        ["", 0],
        ["L", 0],
        ["A", 1],
        ["AAAAAAAAAAAAAAA", 15],
        ["RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL", 16],
        ["AALAAALARAR", 5]
    ]

    for t in tests:
        res = lineUp(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: lineUp({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: lineUp({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
