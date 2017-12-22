#!/usr/local/bin/python
# Code Fights Rock Paper Scissors Problem

from itertools import combinations


def rockPaperScissors(players):
    return sorted([[b, a] for a, b in combinations(players, 2)] +
                  [[a, b] for a, b in combinations(players, 2)])


def main():
    tests = [
        [
            ["trainee", "warrior", "ninja"],
            [["ninja", "trainee"],
             ["ninja", "warrior"],
             ["trainee", "ninja"],
             ["trainee", "warrior"],
             ["warrior", "ninja"],
             ["warrior", "trainee"]]
        ],
        [
            ["macho", "hero"],
            [["hero", "macho"],
             ["macho", "hero"]]
        ]
    ]

    for t in tests:
        res = rockPaperScissors(t[0])
        if t[1] == res:
            print("PASSED: rockPaperScissors({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: rockPaperScissors({}) returned {}, "
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
