#!/usr/local/bin/python
# Code Fights Is IPv4 Address Problem


def isIPv4Address(inputString):
    import re
    pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}$')
    match = re.search(pattern, inputString)
    if match:
        segments = inputString.split(".")
        return sum([int(x) >= 0 and int(x) <= 255 for x in segments]) == 4

    return False


def main():
    tests = [
        ["172.16.254.1", True],
        ["172.316.254.1", False],
        [".254.255.0", False],
        ["1.1.1.1a", False],
        ["1", False],
        ["0.254.255.0", True],
        ["1.23.256.255.", False],
        ["1.23.256..", False],
        ["0..1.0", False],
        ["1.1.1.1.1", False],
        ["1.256.1.1", False],
        ["a0.1.1.1", False],
        ["0.1.1.256", False],
        ["129380129831213981.255.255.255", False],
        ["255.255.255.255abcdekjhf", False],
        ["7283728", False]
    ]

    for t in tests:
        res = isIPv4Address(t[0])
        if t[1] == res:
            print("PASSED: isIPv4Address({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isIPv4Address({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
