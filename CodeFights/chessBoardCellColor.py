#!/usr/local/bin/python
# Code Fights Chess Board Cell Color Problem


def chessBoardCellColor(cell1, cell2):
    '''
    Determine if the two given cells on chess board are same color
    A, C, E, G odd cells are same color as B, D, F, H even cells
    '''
    def get_color(cell):
        return ("DARK" if (cell[0] in "ACEG" and int(cell[1]) % 2 == 1) or
                (cell[0] in "BDFH" and int(cell[1]) % 2 == 0) else "LIGHT")
    return get_color(cell1) == get_color(cell2)


def main():
    tests = [
        ["A1", "C3", True],
        ["A1", "H3", False],
        ["A1", "A2", False],
        ["A1", "B2", True],
        ["B3", "H8", False],
        ["C3", "B5", False],
        ["G5", "E7", True],
        ["C8", "H8", False],
        ["D2", "D2", True],
        ["A2", "A5", False]
    ]

    for t in tests:
        res = chessBoardCellColor(t[0], t[1])
        if t[2] == res:
            print("PASSED: chessBoardCellColor({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: chessBoardCellColor({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
