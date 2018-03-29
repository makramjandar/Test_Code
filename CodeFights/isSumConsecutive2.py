#!/usr/local/bin/python
# Code Fights Is Sum Consecutive 2 Problem


def isSumConsecutive2(n):
    count = 0
    nums = list(range(1, n))
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            tmp = sum(nums[i:j])
            if tmp == n:
                count += 1
            if tmp > n:
                break
    return count


def main():
    tests = [
        # [9, 2],
        # [8, 0],
        [15, 3]
    ]

    for t in tests:
        res = isSumConsecutive2(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isSumConsecutive2({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isSumConsecutive2({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
