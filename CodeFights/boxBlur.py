#!/usr/local/bin/python
# Code Fights Add Border Problem


def boxBlur(image):
    new_image = []
    for r in range(1, len(image) - 1):
        new_row = []
        for c in range(1, len(image[0]) - 1):
            new_row.append(sum([image[r + a][c + b] for a in [-1, 0, 1]
                                for b in [-1, 0, 1]]) // 9)
        new_image.append(new_row)
    return new_image


def main():
    tests = [
        [
            [
                [1, 1, 1],
                [1, 7, 1],
                [1, 1, 1]
            ],
            [
                [1]
            ]
        ],
        [
            [
                [0, 18, 9],
                [27, 9, 0],
                [81, 63, 45]
            ],
            [
                [28]
            ]
        ],
        [
            [
                [36, 0, 18, 9],
                [27, 54, 9, 0],
                [81, 63, 72, 45]
            ],
            [
                [40, 30]
            ]
        ],
        [
            [
                [7, 4, 0, 1],
                [5, 6, 2, 2],
                [6, 10, 7, 8],
                [1, 4, 2, 0]
            ],
            [
                [5, 4],
                [4, 4]
            ]
        ],
        [
            [
                [36, 0, 18, 9, 9, 45, 27],
                [27, 0, 54, 9, 0, 63, 90],
                [81, 63, 72, 45, 18, 27, 0],
                [0, 0, 9, 81, 27, 18, 45],
                [45, 45, 27, 27, 90, 81, 72],
                [45, 18, 9, 0, 9, 18, 45],
                [27, 81, 36, 63, 63, 72, 81]
            ],
            [
                [39, 30, 26, 25, 31],
                [34, 37, 35, 32, 32],
                [38, 41, 44, 46, 42],
                [22, 24, 31, 39, 45],
                [37, 34, 36, 47, 59]
            ]
        ],
    ]

    for t in tests:
        res = boxBlur(t[0])
        if t[1] == res:
            print("PASSED: boxBlur({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: boxBlur({}) returned {}, should have returned {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
