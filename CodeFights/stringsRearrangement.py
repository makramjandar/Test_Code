#!/usr/local/bin/python
# Code Fights Cracking Password Problem
# Bought hint for top Python solution

import itertools


def stringsRearrangement(inputArray):

    def f(x, y):
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        if c == 1:
            return True
        return False

    for k in itertools.permutations(inputArray, len(inputArray)):
        print(k)
        r = True
        for i in range(len(k) - 1):
            if not f(k[i], k[i + 1]):
                r = False
        if r:
            return True

    return False


def main():
    tests = [
        [["aba", "bbb", "bab"], False],
        [["ab", "bb", "aa"], True],
        [["q", "q"], False],
        [["zzzzab", "zzzzbb", "zzzzaa"], True],
        [["ab", "ad", "ef", "eg"], False],
        [["abc", "bef", "bcc", "bec", "bbc", "bdc"], True],
        [["abc", "abx", "axx", "abc"], False],
        [["abc", "abx", "axx", "abx", "abc"], True],
        [["f", "g", "a", "h"], True]
    ]

    for t in tests:
        res = stringsRearrangement(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: stringsRearrangement({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: stringsRearrangement({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
