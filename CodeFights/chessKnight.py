#!/usr/local/bin/python
# Code Fights Chess Knight Problem


def chessKnight(cell):
    # Check it's a valid cell
    import re
    match = re.search(r'^([a-h])([1-8])$', cell, re.I)
    if not bool(match):
        # Invalid cell
        return 0
    file, rank = match.group(1).lower(), int(match.group(2))
    moves = 8
    if file in "ah":
        moves -= 4
        if rank == 2 or rank == 7:
            moves -= 1
        elif rank == 1 or rank == 8:
            moves -= 2
    elif file in "bg":
        moves -= 2
        if rank == 2 or rank == 7:
            moves -= 2
        elif rank == 1 or rank == 8:
            moves -= 3
    elif rank == 2 or rank == 7:
        moves -= 2
    elif rank == 1 or rank == 8:
        moves -= 4

    return moves


def main():
    tests = [
        ["a1", 2],
        ["c2", 6],
        ["d4", 8],
        ["g6", 6],
        ["a10", 0]
    ]

    for t in tests:
        res = chessKnight(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: chessKnight({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: chessKnight({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
