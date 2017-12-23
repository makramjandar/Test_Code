#!/usr/local/bin/python
# Code Fights Kth Permutation Problem

from itertools import permutations


def kthPermutation(numbers, k):
    return list(list(permutations(numbers, len(numbers)))[k - 1])


def main():
    tests = [
        [[1, 2, 3, 4, 5], 4, [1, 2, 4, 5, 3]],
        [[1, 2], 1, [1, 2]],
        [[11, 22, 31, 43, 56], 120, [56, 43, 31, 22, 11]],
        [[14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 238,
            [14, 25, 27, 29, 40, 239, 100, 55, 89, 30]],
        [[14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 3628800,
            [239, 100, 89, 55, 40, 30, 29, 27, 25, 14]],
        [[50, 100, 123, 789], 15, [123, 100, 50, 789]]
    ]

    for t in tests:
        res = kthPermutation(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: kthPermutation({}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: kthPermutation({}, {}) returned {}, "
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
