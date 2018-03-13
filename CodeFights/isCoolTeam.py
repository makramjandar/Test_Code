#!/usr/local/bin/python
# Code Fights Is Cool Team Problem


class Team(object):
    def __init__(self, names):
        self.names = names

    def __call__(self):
        first = [n[0].lower() for n in self.names]
        remaining = [n[-1].lower() for n in self.names]
        count = 0
        for letter in first:
            if letter not in remaining:
                count += 1
            elif letter in remaining:
                remaining.remove(letter)


def isCoolTeam(team):
    return bool(Team(team))


def main():
    tests = [
        [["Mark", "Kelly", "Kurt", "Terk"], True],
        [["Lucy"], True],
        [["Rob", "Bobby", "Billy"], False],
        [["Sophie", "Boris", "EriC", "Charlotte"], True],
        [["Sophie", "Boris", "Eric", "Charlotte", "Charlie"], False],
        [["Sophie", "Edward", "Deb", "Boris", "Stephanie", "Eric", "Charlotte",
          "Eric", "Charlie"], True],
        [["Bobo", "obob", "Bobo", "ob"], True],
        [["Edward", "Daniel", "Lily"], True],
        [["ANTONY", "James"], False],
        [["Ned", "Ben"], True]
    ]

    for t in tests:
        res = isCoolTeam(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: isCoolTeam({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: isCoolTeam({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
