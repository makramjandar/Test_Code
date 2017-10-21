#!/usr/local/bin/python
#  Code Fights Reverse Parentheses Problem


def reverseParentheses(s):
    import re

    def reverseS(s):
        pattern = re.compile(r'\(([^()]*)\)')
        match = re.search(pattern, s)
        capturedRev = match.group(1)[::-1]  # first captured group, reversed
        return s.replace(match.group(0), capturedRev)

    if (s.find('(') != -1):
        return reverseParentheses(reverseS(s))
    else:
        return s


# def reverseParentheses(s):
#     'Recursive - assumes all parentheses are nested'
#     if (s.find('(') == -1):
#         return s
#     else:
#         firstParens = s.find('(')
#         lastParens = max([i for i, char in enumerate(s) if char == ')'])
#         return (s[:firstParens] +
#                 reverseParentheses(s[firstParens + 1:lastParens])[::-1] +
#                s[lastParens + 1:])


def main():
    tests = [
        ["co(de(fight)s)", "cosfighted"],
        ["a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"],
        ["abc(cba)ab(bac)c", "abcabcabcabc"]
    ]

    for t in tests:
        print("TESTING: {}".format(t[0]))
        t1 = reverseParentheses(t[0])
        if (t1 == t[1]):
            print("PASSED: {}".format(t1))
        else:
            print("FAILED: {}".format(t1))


if __name__ == '__main__':
    main()
