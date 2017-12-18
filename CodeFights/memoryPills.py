#!/usr/local/bin/python
# Code Fights Mirror Bits (Core) Problem

from itertools import dropwhile


def memoryPills(pills):
    gen = dropwhile(lambda p: len(p) % 2 == 1, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]


def main():
    tests = [
        [["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen",
          "Superpillsus"], ["Bestmedicen", "Superpillsus", ""]],
        [["Pillin"], ["", "", ""]],
        [["Med 1", "Med 2", "Med 3", "Med 10", "Med 11", "Med 12", "Med 14",
          "Med 42", "Med 239"], ["Med 11", "Med 12", "Med 14"]],
        [["Pills", "Shmills", "Medicine", "Phedicine", "Hey", "Hoy"],
         ["Phedicine", "Hey", "Hoy"]],
        [["Test", "Where", "The", "First", "Element", "Is", "Even"],
         ["Where", "The", "First"]]
    ]

    for t in tests:
        res = memoryPills(t[0])
        if t[1] == res:
            print("PASSED: memoryPills({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: memoryPills({}) returned {},"
                   "answer: {}").format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
