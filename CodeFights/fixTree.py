#!/usr/local/bin/python
# Code Fights Fix Tree Problem


def fixTree(tree):
    return [s.strip().center(len(s)) for s in tree]


def main():
    tests = [
        [
            ["      *  ",
             "    *    ",
             "***      ",
             "    *****",
             "  *******",
             "*********",
             " ***     "],
            ["    *    ",
             "    *    ",
             "   ***   ",
             "  *****  ",
             " ******* ",
             "*********",
             "   ***   "]
        ],
        [
            ["    *    ",
             "    *    ",
             "   ***   ",
             "  *****  ",
             " ******* ",
             "*********",
             "   ***   "],
            ["    *    ",
             "    *    ",
             "   ***   ",
             "  *****  ",
             " ******* ",
             "*********",
             "   ***   "]
        ],
        [
            ["*",
             "*",
             "*",
             "*"],
            ["*",
             "*",
             "*",
             "*"]
        ],
        [
            ["   *** "],
            ["  ***  "]
        ],
        [
            ["         *   ",
             "*            ",
             "       ***   ",
             "   *****     ",
             "  *******    ",
             "  *********  ",
             "*******      ",
             "   ********* ",
             "  ***********",
             "    *********",
             "***********  ",
             "*************",
             "        ***  ",
             "  ***        ",
             "       ***   "],
            ["      *      ",
             "      *      ",
             "     ***     ",
             "    *****    ",
             "   *******   ",
             "  *********  ",
             "   *******   ",
             "  *********  ",
             " *********** ",
             "  *********  ",
             " *********** ",
             "*************",
             "     ***     ",
             "     ***     ",
             "     ***     "]
        ]
    ]

    for t in tests:
        res = fixTree(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: fixTree({}) returned {}"
                  .format(t[0], res))
        else:
            print(("FAILED: fixTree({}) returned {},"
                   "answer: {}").format(t[0], res, ans))


if __name__ == '__main__':
    main()
