#!/usr/local/bin/python
# Code Fights Primary School Problem


class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.height * self.width

    @area.setter
    def area(self):
        self.area = self.height * self.width


def primarySchool(height, width):
    return str(Rectangle(height, width))


def main():
    tests = [
        [7, 4, "7 x 4 = 28"],
        [1, 20, "1 x 20 = 20"],
        [3, 13, "3 x 13 = 39"],
        [10, 3, "10 x 3 = 30"],
        [16, 12, "16 x 12 = 192"]
    ]

    for t in tests:
        res = primarySchool(t[0], t[1])
        ans = t[2]
        if ans == res:
            print("PASSED: primarySchool({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: primarySchool({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, ans))


if __name__ == '__main__':
    main()
