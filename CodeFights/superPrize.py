#!/usr/local/bin/python
# Code Fights Super Prize Problem


class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d
        self.eligible = [j + 1 for j, item in enumerate(self.purchases) if
                         (j + 1) % self.n == 0 and item % self.d == 0]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.i < len(self.eligible)):
            curr, self.i = self.i, self.i + 1
            return self.eligible[curr]
        else:
            raise StopIteration


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))


def main():
    tests = [
        [[12, 43, 13, 465, 1, 13], 2, 3, [4]],
        [[], 2, 2, []],
        [
            [988, 126, 876, 615, 323, 835, 815, 2, 867, 952, 95, 397, 546,
             762, 350],
            17,
            7,
            []
        ],
        [
            [41, 51, 91, 72, 71, 30, 28, 35, 55, 62, 65, 45, 100, 54, 83, 69,
             66, 43],
            2,
            5,
            [6, 8, 12]
        ],
        [
            [64, 67, 86, 87, 69, 49, 47, 75, 43, 74, 23, 47, 77, 83, 67, 24,
             11, 59, 19, 88],
            4,
            5,
            [8]
        ]
    ]

    for t in tests:
        res = superPrize(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: superPrize({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print("FAILED: superPrize({}, {}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
