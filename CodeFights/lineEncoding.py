#!/usr/local/bin/python
# Code Fights Line Encoding Problem

import re


def lineEncoding(s):
    return re.sub(r"(.)\1+", lambda m: str(len(m.group(0))) + m.group(1), s)


def main():
    tests = [
        ["aabbbc", "2a3bc"],
        ["abbcabb", "a2bca2b"],
        ["abcd", "abcd"]
    ]

    for t in tests:
        res = lineEncoding(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: lineEncoding({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: lineEncoding({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
