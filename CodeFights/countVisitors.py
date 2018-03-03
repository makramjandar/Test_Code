#!/usr/local/bin/python
# Code Fights Count Visitors Problem


class Counter(object):
    def __init__(self, value):
        self.value = value

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()


def main():
    tests = [
        [22, 5, [4, 6, 6, 5, 2, 2, 5], 26],
        [1, 5, [], 1],
        [34, 8, [1, 2, 3, 4, 5, 6, 7], 34],
        [4, 5, [3, 4, 65, 3, 2, 4, 5, 3, 5], 7],
        [38, 20, [20], 39]
    ]

    for t in tests:
        res = countVisitors(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: countVisitors({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: countVisitors({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
