#!/usr/local/bin/python
# Code Fights Crazyball Problem

from itertools import combinations


def crazyball(players, k):
    return sorted([sorted(list(l)) for l in combinations(players, k)])


def main():
    tests = [
        [["Ninja", "Warrior", "Trainee", "Newbie"], 3,
            [["Newbie", "Ninja", "Trainee"], ["Newbie", "Ninja", "Warrior"],
             ["Newbie", "Trainee", "Warrior"],
             ["Ninja", "Trainee", "Warrior"]]],
        [["Ninja", "Warrior", "Trainee", "Newbie"], 4,
            [["Newbie", "Ninja", "Trainee", "Warrior"]]],
        [["Pooh"], 1, [["Pooh"]]],
        [["Browny", "Whitey", "Blacky"], 1,
            [["Blacky"], ["Browny"], ["Whitey"]]],
        [["One", "Two", "Three", "Four", "Five", "Six", "Seven"], 5,
            [["Five", "Four", "One", "Seven", "Six"],
             ["Five", "Four", "One", "Seven", "Three"],
             ["Five", "Four", "One", "Seven", "Two"],
             ["Five", "Four", "One", "Six", "Three"],
             ["Five", "Four", "One", "Six", "Two"],
             ["Five", "Four", "One", "Three", "Two"],
             ["Five", "Four", "Seven", "Six", "Three"],
             ["Five", "Four", "Seven", "Six", "Two"],
             ["Five", "Four", "Seven", "Three", "Two"],
             ["Five", "Four", "Six", "Three", "Two"],
             ["Five", "One", "Seven", "Six", "Three"],
             ["Five", "One", "Seven", "Six", "Two"],
             ["Five", "One", "Seven", "Three", "Two"],
             ["Five", "One", "Six", "Three", "Two"],
             ["Five", "Seven", "Six", "Three", "Two"],
             ["Four", "One", "Seven", "Six", "Three"],
             ["Four", "One", "Seven", "Six", "Two"],
             ["Four", "One", "Seven", "Three", "Two"],
             ["Four", "One", "Six", "Three", "Two"],
             ["Four", "Seven", "Six", "Three", "Two"],
             ["One", "Seven", "Six", "Three", "Two"]]]
    ]

    for t in tests:
        res = crazyball(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: crazyball({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print(("FAILED: crazyball({}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
