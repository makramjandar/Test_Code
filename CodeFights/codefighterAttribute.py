#!/usr/local/bin/python
# Code Fights Codefighter Attribute Problem


class CodeFighter(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, attribute, default=None):
        if default is None:
            default = "{} attribute is not defined".format(attribute)
        if attribute not in self.__dir__():
            return default
        else:
            return self.attribute


def codefighterAttribute(attribute):
    codefighter = CodeFighter("annymaster", "1234567", "1500", "anny")
    return getattr(codefighter, attribute)


def main():
    tests = [
        ["_id", "1234567"],
        ["age", "age attribute is not defined"],
        ["name", "anny"],
        ["country", "country attribute is not defined"],
        ["I", "I attribute is not defined"]
    ]

    for t in tests:
        res = codefighterAttribute(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: codefighterAttribute({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: codefighterAttribute({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
