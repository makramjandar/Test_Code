#!/usr/local/bin/python
# Code Fights Is Cool Team Problem


class Team(object):
    def __init__(self, names):
        self.names = names

    def __call__(self, team):
        choices = [(p[0].lower(), p[-1].lower()) for p in team]
        print("People: {}".format(choices))

        # Helper functions
        def get_neighbs(person, choices):
            """
            person: a tuple ("first letter", "last letter")
            choices: a list of tuples in same format
            Returns a list of tuples where choices start with the same letter
                that person ended with
            """
            return [p for p in choices if p[0] == person[-1]]

        def longest_path_from(person, choices):
            choices = choices.remove(person)
            neighbors = get_neighbs(person, choices)

            if neighbors:
                paths = (longest_path_from(p, choices) for p in neighbors)
                max_path = max(paths, key=len)
            else:
                max_path = []

            return [person] + max_path

        def longest_path(choices):
            return max((longest_path_from(p, choices) for p in choices),
                       key=len)

        if len(team) <= 1:
            return True
        else:
            lp = longest_path(choices)
            print("Longest path: {}".format(lp))
            return lp == len(team)


def isCoolTeam(team):
    return bool(Team(team))


def main():
    tests = [
        # [["Mark", "Kelly", "Kurt", "Terk"], True],
        [["Lucy"], True],
        [["Rob", "Bobby", "Billy"], False],
        # [["Sophie", "Boris", "EriC", "Charlotte"], True],
        [["Sophie", "Boris", "Eric", "Charlotte", "Charlie"], False],
        # [["Sophie", "Edward", "Deb", "Boris", "Stephanie", "Eric", "Charlotte",
          # "Eric", "Charlie"], True],
        [["Bobo", "obob", "Bobo", "ob"], True],
        # [["Edward", "Daniel", "Lily"], True],
        [["ANTONY", "James"], False],
        # [["Ned", "Ben"], True]
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
