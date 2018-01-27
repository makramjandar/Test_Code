#!/usr/local/bin/python
# Code Fights Is MAC48 Address Problem


def isMAC48Address(inputString):
    import re
    pattern = re.compile(r'^(?:[A-Fa-f0-9]{1,2}-){5}(?:[A-Fa-f0-9]{1,2})$')
    return bool(re.search(pattern, inputString))


def main():
    tests = [
        ["00-1B-63-84-45-E6", True],
        ["Z1-1B-63-84-45-E6", False],
        ["not a MAC-48 address", False],
        ["FF-FF-FF-FF-FF-FF", True],
        ["00-00-00-00-00-00", True],
        ["G0-00-00-00-00-00", False],
        ["02-03-04-05-06-07-", False],
        ["12-34-56-78-9A-BC", True],
        ["FF-FF-AB-CD-EA-BC", True],
        ["12-34-56-78-9A-BG", False]
    ]

    for t in tests:
        res = isMAC48Address(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isMAC48Address({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isMAC48Address({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
