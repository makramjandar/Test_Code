#!/usr/local/bin/python
# Code Fights Election Winners Problem


def electionsWinners(votes, k):
    max_v = max(votes)
    count_max = votes.count(max_v)
    if k == 0:
        if count_max == 1:
            return 1
        else:
            return 0
    return sum([1 for v in votes if v + k > max_v])

    # Alternative solution:
    # max_v = max(votes)
    # return (int(votes.count(max_v) == 1) if k == 0 else
    #         len([n for n in votes if max_v < n + k]))


def main():
    tests = [
        [[2, 3, 5, 2], 3, 2],
        [[1, 3, 3, 1, 1], 0, 0],
        [[5, 1, 3, 4, 1], 0, 1],
        [[1, 1, 1, 1], 1, 4],
        [[1, 1, 1, 1], 0, 0],
        [[3, 1, 1, 3, 1], 2, 2]
    ]

    for t in tests:
        res = electionsWinners(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: electionsWinners({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: electionsWinners({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
