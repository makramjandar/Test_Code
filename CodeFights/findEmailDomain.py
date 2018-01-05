#!/usr/local/bin/python
# Code Fights Find Email Domain Problem


def findEmailDomain(address):
    index = max([i for i, char in enumerate(address) if char == "@"])
    return address[index + 1:]


def main():
    tests = [
        ["prettyandsimple@example.com", "example.com"],
        ["<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org", "example.org"],
        ["someaddress@yandex.ru", "yandex.ru"],
        ["\" \"@xample.org", "xample.org"]
    ]

    for t in tests:
        res = findEmailDomain(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: findEmailDomain({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: findEmailDomain({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
