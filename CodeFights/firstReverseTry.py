#!/usr/local/bin/python
# Code Fights First Reverse Try Problem


def firstReverseTry(arr):
    if len(arr) > 1:
        first, *m, last = arr
        return [last] + m + [first]
    else:
        return arr


def main():
    tests = [
        [[1, 2, 3, 4, 5], [5, 2, 3, 4, 1]],
        [[], []],
        [[239], [239]],
        [
            [23, 54, 12, 3, 4, 56, 23, 12, 5, 324],
            [324, 54, 12, 3, 4, 56, 23, 12, 5, 23]
        ],
        [[-1, 1], [1, -1]],
        [
            [88, -101, -310, 818, 747, -888, -183, -687, -723, 188, -611, 677,
             -597, 293, -295, -162, -265, 368, 346, 81, -831, 198, -94, 685,
             -434, -241, -566, -397, 501, -183, 366, -669, 96, -592, 358, 598,
             444, -929, 769, -361, -754, 218, -464, 332, 893, 422, -192, -287,
             -850, 543],
            [543, -101, -310, 818, 747, -888, -183, -687, -723, 188, -611, 677,
             -597, 293, -295, -162, -265, 368, 346, 81, -831, 198, -94, 685,
             -434, -241, -566, -397, 501, -183, 366, -669, 96, -592, 358, 598,
             444, -929, 769, -361, -754, 218, -464, 332, 893, 422, -192, -287,
             -850, 88]
        ]
    ]

    for t in tests:
        res = firstReverseTry(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: firstReverseTry({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: firstReverseTry({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
