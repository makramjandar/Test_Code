#!/usr/local/bin/python
# Code Fights Addition Without Carrying Problem


def additionWithoutCarrying(param1, param2):
    s1, s2 = str(param1), str(param2)
    shorter = s1 if len(s1) < len(s2) else s2
    longer = s2 if shorter == s1 else s1
    if len(shorter) < len(longer):
        shorter = shorter.zfill(len(longer))
    return int(''.join([str(int(a) + int(b))[-1] for (a, b) in
                        zip(shorter, longer)]))


def main():
    tests = [
        [456, 1734, 1180],
        [99999, 0, 99999],
        [999, 999, 888],
        [0, 0, 0],
        [54321, 54321, 8642]
    ]

    for t in tests:
        res = additionWithoutCarrying(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: additionWithoutCarrying({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: additionWithoutCarrying({}, {}) returned {},"
                  "answer: {}".format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
