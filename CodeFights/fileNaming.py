#!/usr/local/bin/python
# Code Fights File Naming Problem


def fileNaming(names):
    valid = []
    tmp = dict()
    for name in names:
        if name not in tmp:
            valid.append(name)
            tmp[name] = True
        else:
            # That file name has been used
            k = 1
            new = name
            while new in tmp:
                new = name + '(' + str(k) + ')'
                k += 1
            valid.append(new)
            tmp[new] = True
    return valid


def main():
    tests = [
        [
            ["doc", "doc", "image", "doc(1)", "doc"],
            ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
        ],
        [
            ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
            ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)",
             "a(8)", "a(9)", "a(10)", "a(11)"]
        ],
        [
            ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)",
             "dd", "dd(1)"],
            ["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", "dd(1)(2)",
             "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"]
        ]
    ]

    for t in tests:
        res = fileNaming(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: fileNaming({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: fileNaming({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
