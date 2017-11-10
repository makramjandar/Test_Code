#!/usr/local/bin/python
# Code Fights Add Border Problem


def minesweeper(matrix):
    '''
    Convert minesweeper matrix showing True if mine in that cell, False
        otherwise into a matrix with counts of how many neighboring mines.
        Neighbor is a cell that shares at least a corner.
    '''
    num_mines = []
    rows = len(matrix)
    cols = len(matrix[0])
    adj = [-1, 0, 1]
    for r in range(rows):
        curr_row = []
        for c in range(cols):
            # Add neighboring cells if not out of bounds or cell itself
            curr_row.append(sum([matrix[r + i][c + j] for i in adj
                                 if (r + i >= 0 and r + i < rows) for j in adj
                                 if (c + j >= 0 and c + j < cols and
                                     not(i == 0 and j == 0))]))
        num_mines.append(curr_row)

    return num_mines


def main():
    tests = [
        [
            [
                [True, False, False],
                [False, True, False],
                [False, False, False]
            ],
            [
                [1, 2, 1],
                [2, 1, 1],
                [1, 1, 1]
            ]
        ],
        [
            [
                [False, False, False],
                [False, False, False]
            ],
            [
                [0, 0, 0],
                [0, 0, 0]
            ]
        ],
        [
            [
                [True, False, False, True],
                [False, False, True, False],
                [True, True, False, True]
            ],
            [
                [0, 2, 2, 1],
                [3, 4, 3, 3],
                [1, 2, 3, 1]
            ]
        ]
    ]

    for t in tests:
        res = minesweeper(t[0])
        if t[1] == res:
            print("PASSED: minesweeper({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: minesweeper({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
