#!/usr/local/bin/Python3

from vector import Vector
from line import Line


def main():
    test_intersections = True

    # Test if lines are parallel, same, or have an intersection
    if test_intersections:
        print("\n=== Parallel, Same, or Intersecting Lines Quiz ===\n")

        l_1 = Line(Vector([4.046, 2.836]), 1.21)
        l_2 = Line(Vector([10.115, 7.09]), 3.025)
        print(l_1)
        print(l_2)
        print("Parallel: {}".format(l_1.is_parallel(l_2)))
        print("Same line: {}".format(l_1 == l_2))
        print("Intersection: {}\n".format(l_1.intersection(l_2)))

        l_3 = Line(Vector([7.204, 3.182]), 8.68)
        l_4 = Line(Vector([8.172, 4.114]), 9.883)
        print(l_3)
        print(l_4)
        print("Parallel: {}".format(l_3.is_parallel(l_4)))
        print("Same line: {}".format(l_3 == l_4))
        print("Intersection: {}\n".format(l_3.intersection(l_4)))

        l_5 = Line(Vector([1.182, 5.562]), 6.744)
        l_6 = Line(Vector([1.773, 8.343]), 9.525)
        print(l_5)
        print(l_6)
        print("Parallel: {}".format(l_5.is_parallel(l_6)))
        print("Same line: {}".format(l_5 == l_6))
        print("Intersection: {}\n".format(l_5.intersection(l_6)))


if __name__ == '__main__':
    main()
