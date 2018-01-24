#!/usr/local/bin/python
# Code Fights Range Float Problem


class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if ((self.step > 0 and self.i < self.stop) or
                (self.step < 0 and self.i > self.stop)):
            tmp, self.i = self.i, self.i + self.step
            return tmp
        else:
            raise StopIteration


def rangeFloat(args):
    return list(FRange(*args))


def main():
    tests = [
        [[5], [0, 1, 2, 3, 4]],
        [[0.5, 7.5], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]],
        [
            [-1.1, 2.4, 0.3],
            [-1.1, -0.8, -0.5, -0.2, 0.1, 0.4, 0.7, 1, 1.3, 1.6, 1.9, 2.2]
        ],
        [[5.6, 3.2], []],
        [[-3.2, -123, 10], []],
        [[-4], []],
        [[10.4, 3.2, -1.2], [10.4, 9.2, 8, 6.8, 5.6, 4.4, 3.2]],
        [[10, 10, 3], []],
        [
            [33.3],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        ]
    ]

    for t in tests:
        res = rangeFloat(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: rangeFloat({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: rangeFloat({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
