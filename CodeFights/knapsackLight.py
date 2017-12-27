#!/usr/local/bin/python
# Code Fights Knapsack Problem


def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        return max([v for v, w in zip((value1, value2), (weight1, weight2))
                   if w <= maxW] + [0])


def main():
    tests = [
        [10, 5, 6, 4, 8, 10],
        [10, 5, 6, 4, 9, 16],
        [5, 3, 7, 4, 6, 7],
        [10, 2, 11, 3, 1, 0],
        [15, 2, 20, 3, 2, 15],
        [2, 5, 3, 4, 5, 3],
        [4, 3, 3, 4, 4, 4],
        [3, 5, 3, 8, 10, 3]
    ]

    for t in tests:
        res = knapsackLight(t[0], t[1], t[2], t[3], t[4])
        ans = t[5]
        if ans == res:
            print("PASSED: knapsackLight({}, {}, {}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], t[3], t[4], res))
        else:
            print(("FAILED: knapsackLight({}, {}, {}, {}, {}) returned {},"
                   "answer: {}")
                  .format(t[0], t[1], t[2], t[3], t[4], res, ans))


if __name__ == '__main__':
    main()
