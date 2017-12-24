#!/usr/local/bin/python
# Code Fights Array Max Consecutive Sum Problem


def arrayMaxConsecutiveSum(inputArray, k):
    rolling_sum = sum(inputArray[:k])
    max_sum = rolling_sum
    i = 0
    for j in range(k, len(inputArray)):
        rolling_sum = rolling_sum + inputArray[j] - inputArray[i]
        max_sum = max(rolling_sum, max_sum)
        i += 1

    return max_sum


def main():
    tests = [
        [[2, 3, 5, 1, 6], 2, 8],
        [[2, 4, 10, 1], 2, 14],
        [[1, 3, 2, 4], 3, 9],
        [[3, 2, 1, 1], 1, 3]
    ]

    for t in tests:
        res = arrayMaxConsecutiveSum(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: arrayMaxConsecutiveSum({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: arrayMaxConsecutiveSum({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
