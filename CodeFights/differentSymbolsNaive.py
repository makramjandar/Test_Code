#!/usr/local/bin/python
# Code Fights Different Symbols Naive Problem

from collections import Counter


def differentSymbolsNaive(s):
    return len(Counter(s))


def main():
    tests = [
        ["cabca", 3],
        ["aba", 2]
    ]

    for t in tests:
        res = differentSymbolsNaive(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: differentSymbolsNaive({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: differentSymbolsNaive({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
