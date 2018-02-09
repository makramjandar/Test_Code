#!/usr/local/bin/python
# Code Fights Spiral Numbers Problem


def spiralNumbers(n):
    r, c = 0, 0  # Starting location
    # Delta for row or column increments: first direction is left to right
    dr, dc = 0, 1
    spiral = [[0] * n for _ in range(n)]
    for i in range(1, n * n + 1):
        spiral[r][c] = i
        testr, testc = r + dr, c + dc
        if 0 <= testr < n and 0 <= testc < n and spiral[testr][testc] == 0:
            r, c = testr, testc
        else:
            dr, dc = dc, -dr
            r, c = r + dr, c + dc
    return spiral


def main():
    tests = [
        [
            3,
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        ],
        [
            5,
            [[1, 2, 3, 4, 5],
             [16, 17, 18, 19, 6],
             [15, 24, 25, 20, 7],
             [14, 23, 22, 21, 8],
             [13, 12, 11, 10, 9]]
        ],
        [
            6,
            [[1, 2, 3, 4, 5, 6],
             [20, 21, 22, 23, 24, 7],
             [19, 32, 33, 34, 25, 8],
             [18, 31, 36, 35, 26, 9],
             [17, 30, 29, 28, 27, 10],
             [16, 15, 14, 13, 12, 11]]
        ]
    ]

    for t in tests:
        res = spiralNumbers(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: spiralNumbers({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: spiralNumbers({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
