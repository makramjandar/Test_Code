#!/usr/local/bin/python
# Code Fights Weak Numbers Problem


def weakNumbers(n):
    def get_divisors(n):
        divs = []
        for i in range(1, n + 1):
            count = 0
            for d in range(1, i + 1):
                if i % d == 0:
                    count += 1
            divs.append(count)
        return divs

    divs = get_divisors(n)
    w = []


def main():
    tests = [
        [9, [2, 2]],
        [1, [0, 1]],
        [2, [0, 2]],
        [7, [2, 1]],
        [500, [403, 1]],
        [4, [0, 4]]
    ]

    for t in tests:
        res = weakNumbers(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: weakNumbers({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: weakNumbers({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
