#!/usr/local/bin/python
# Code Fights Create Die Problem

import random


def createDie(seed, n):
    class Die(object):
        def __new__(self, seed, n):
            random.seed(seed)
            return int(random.random() * n) + 1

    class Game(object):
        die = Die(seed, n)

    return Game.die


def main():
    tests = [
        [37237, 5, 3],
        [36706, 12, 9],
        [21498, 10, 10],
        [2998, 6, 3],
        [5509, 10, 4]
    ]

    for t in tests:
        res = createDie(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: createDie({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: createDie({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
