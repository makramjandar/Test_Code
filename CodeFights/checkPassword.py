#!/usr/local/bin/python
# Code Fights Check Password Problem


def checkPassword(attempts, password):
    def check():
        while True:
            tmp = yield
            yield tmp == password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1


def main():
    tests = [
        [["hello", "world", "I", "like", "coding"], "like", 4],
        [["hello", "world", "I", "like", "coding"], "qwerty123", -1],
        [["codefights"], "codefights", 1],
        [["123", "456", "qwerty", "zzz", "password", "genius239", "password"],
            "password", 5],
        [["warrior", "ninja", "trainee"], "recruit", -1],
        [[], "igiveup", -1]
    ]

    for t in tests:
        res = checkPassword(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: checkPassword({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: checkPassword({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
