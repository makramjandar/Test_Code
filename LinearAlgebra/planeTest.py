#!/usr/local/bin/Python3

from vector import Vector
from plane import Plane


def main():
    test_parallel_or_same = True

    # Test if planes are parallel, same, or have an intersection
    if test_parallel_or_same:
        print("\n=== Parallel or Same Planes Quiz ===\n")

        p_1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
        p_2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
        print(p_1)
        print(p_2)
        print("Parallel: {}".format(p_1.is_parallel(p_2)))
        print("Same plane: {}\n".format(p_1 == p_2))

        p_3 = Plane(Vector([2.611, 5.528, 0.283]), 4.60)
        p_4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
        print(p_3)
        print(p_4)
        print("Parallel: {}".format(p_3.is_parallel(p_4)))
        print("Same plane: {}\n".format(p_3 == p_4))

        p_5 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
        p_6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
        print(p_5)
        print(p_6)
        print("Parallel: {}".format(p_5.is_parallel(p_6)))
        print("Same plane: {}\n".format(p_5 == p_6))


if __name__ == '__main__':
    main()
