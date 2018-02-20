#!/usr/local/bin/python
# Code Fights Merging Vines Problem


def mergingVines(vines, n):
    def nTimes(n):
        def func_decor(func):
            def func_wrapper(vines):
                for _ in range(n):
                    vines = func(vines)
                return vines
            return func_wrapper
        return func_decor

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)


def main():
    tests = [
        [[1, 2, 3, 4, 5], 2, [10, 5]],
        [[1, 2, 3, 4, 5, 6], 10, [21]],
        [[5], 4, [5]],
        [[43, 54, 8, 12, 0, 12, 7, 7, 4], 0, [43, 54, 8, 12, 0, 12, 7, 7, 4]],
        [[13, 11, 9, 5, 7, 5, 12, 10, 1, 2, 11, 2, 10, 10, 18, 16, 20, 13, 9,
          100], 4, [142, 142]]
    ]

    for t in tests:
        res = mergingVines(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: mergingVines({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: mergingVines({}, {}) returned {},"
                  "answer: {}".format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
