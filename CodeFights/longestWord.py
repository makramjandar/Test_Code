#!/usr/local/bin/python
# Code Fights Longest Word Problem

import re


def longestWord(text):
    m = re.findall(r'\b[a-z]+?\b', text, flags=re.I)
    return max(m, key=len)


def main():
    tests = [
        ["Ready, steady, go!", "steady"],
        ["Ready[[[, steady, go!", "steady"],
        ["ABCd", "ABCd"]
    ]

    for t in tests:
        res = longestWord(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: longestWord({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: longestWord({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
