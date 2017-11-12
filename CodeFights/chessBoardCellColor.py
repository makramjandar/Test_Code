#!/usr/local/bin/python
# Code Fights Chess Board Cell Color Problem


def chessBoardCellColor(cell1, cell2):
    pass


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
