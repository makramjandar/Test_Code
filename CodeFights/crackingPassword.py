#!/usr/local/bin/python
# Code Fights Cracking Password Problem

from itertools import product


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([s for s in [''.join(digs) for digs in
                  product(createNumber(digits), repeat=k)] if int(s) % d == 0])

    # Alternative solution:
    # return list(filter(lambda x: int(x) % d == 0, map(createNumber,
    #             product(sorted(digits), repeat = k))))


def main():
    tests = [
        [[1, 5, 2], 2, 3, ["12", "15", "21", "51"]],
        [[4, 6, 0, 3], 4, 13,
            ["0000", "0364", "0403", "0663", "3003", "3406", "3640", "3666",
             "4004", "4030", "4043", "4303", "4433", "4446", "6006", "6344",
             "6604", "6630", "6643"]],
        [[1], 4, 11, ["1111"]],
        [[8, 9], 3, 10, []],
        [[4, 6, 0], 1, 7, ["0"]],
        [[3], 9, 3, ["333333333"]]
    ]

    for t in tests:
        res = crackingPassword(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: crackingPassword({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: crackingPassword({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
