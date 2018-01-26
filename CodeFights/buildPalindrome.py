#!/usr/local/bin/python
# Code Fights Build Palindrome Problem


def buildPalindrome(st):
    if st == st[::-1]:
        return st
    for i in range(len(st)):
        s = st + st[i::-1]
        if s == s[::-1]:
            return s


def main():
    tests = [
        ["abcdc", "abcdcba"],
        ["ababab", "abababa"],
        ["abba", "abba"],
        ["abaa", "abaaba"]
    ]

    for t in tests:
        res = buildPalindrome(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: buildPalindrome({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: buildPalindrome({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
