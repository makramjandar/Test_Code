#!/usr/local/bin/python
# Code Fights Is Cool Team Problem


class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):  # 11
        first = [x[0].lower() for x in self.names]
        last = [x[-1].lower() for x in self.names]

        for f in first:
            try:
                last.remove(f)
            except:
                pass
        print("Result of len(last) == 1 is: {}".format(len(last) == 1))
        return len(last) <= 1


class Team_OLD(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self, names):
        choices = [(p[0].lower(), p[-1].lower()) for p in names]
        print("People: {}".format(choices))

        if len(names) <= 1:
            return True
        else:
            lp = self.longest_path(choices)
            print("Longest path: {}".format(lp))
            print("Result is len(lp) ({}) == len(names) ({}) is {}"
                  .format(len(lp), len(names), len(lp) == len(names)))
            return len(lp) == len(names)

    def get_neighbs(self, person, choices):
        """
        person: a tuple ("first letter", "last letter")
        choices: a list of tuples in same format
        Returns a list of tuples where choices start with the same letter
            that person ended with
        """
        print("In get_neighbs, p: {}, choices: {}".format(person, choices))
        if choices is None:
            print("No choices?")
            return []
        return [p for p in choices if p[0] == person[-1]]

    def longest_path_from(self, person, choices):
        choices = choices.remove(person)
        neighbors = self.get_neighbs(person, choices)

        if neighbors:
            paths = (self.longest_path_from(p, choices) for p in neighbors)
            max_path = max(paths, key=len)
        else:
            max_path = []

        return [person] + max_path

    def longest_path(self, choices):
        return max((self.longest_path_from(p, choices) for p in choices),
                   key=len)


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
