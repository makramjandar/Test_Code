#!/usr/local/bin/python
# Code Fights Different Squares Problem


def differentSquares(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if rows < 2 or cols < 2:
        return 0
    s = [[matrix[r + i][c + j] for i in [0, 1] for j in [0, 1]] for r in
         range(rows - 1) for c in range(cols - 1)]
    return len(set([tuple(x) for x in s]))


def main():
    tests = [
        [
            [[3]],
            0
        ],
        [
            [[1, 2, 1],
             [2, 2, 2],
             [2, 2, 2],
             [1, 2, 3],
             [2, 2, 1]],
            6
        ],
        [
            [[9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9]],
            1
        ],
        [
            [[3, 4, 5, 6, 7, 8, 9]],
            0
        ],
        [
            [[3], [4], [5], [6], [7]],
            0
        ],
        [
            [[2, 5, 3, 4, 3, 1, 3, 2],
             [4, 5, 4, 1, 2, 4, 1, 3],
             [1, 1, 2, 1, 4, 1, 1, 5],
             [1, 3, 4, 2, 3, 4, 2, 4],
             [1, 5, 5, 2, 1, 3, 1, 1],
             [1, 2, 3, 3, 5, 1, 2, 4],
             [3, 1, 4, 4, 4, 1, 5, 5],
             [5, 1, 3, 3, 1, 5, 3, 5],
             [5, 4, 4, 3, 5, 4, 4, 4]],
            54
        ],
        [[[1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 9, 9, 9, 2, 3, 9]], 0]
    ]

    for t in tests:
        res = differentSquares(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: differentSquares({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: differentSquares({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
