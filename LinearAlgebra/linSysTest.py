#!/Applications/anaconda/envs/Python3/bin

from vector import Vector
from plane import Plane
from linsys import LinearSystem


def main():
    test_row_ops = False
    test_triangular_form = True

    # Test row operations: swap rows, multiply row by number, add a multiple times one row to another
    if test_row_ops:
        print("\n=== Row Operations Quiz ===\n")

        p0 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p1 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
        p2 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
        p3 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)

        s = LinearSystem([p0,p1,p2,p3])
        s.swap_rows(0,1)
        if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
            print("Failed test case 1")
        else:
            print("Passed test case 1")

        s.swap_rows(1,3)
        if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
            print("Failed test case 2")
        else:
            print("Passed test case 2")

        s.swap_rows(3,1)
        if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
            print("Failed test case 3")
        else:
            print("Passed test case 3")

        s.multiply_coefficient_and_row(1,0)
        if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
            print("Failed test case 4")
        else:
            print("Passed test case 4")

        s.multiply_coefficient_and_row(-1,2)
        if not (s[0] == p1 and
                s[1] == p0 and
                s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
                s[3] == p3):
            print("Failed test case 5")
        else:
            print("Passed test case 5")

        s.multiply_coefficient_and_row(10,1)
        if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10,10,10]), constant_term=10) and
                s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
                s[3] == p3):
            print("Failed test case 6")
        else:
            print("Passed test case 6")

        s.add_multiple_times_row_to_row(0,0,1)
        if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10,10,10]), constant_term=10) and
                s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
                s[3] == p3):
            print("Failed test case 7")
        else:
            print("Passed test case 7")

        s.add_multiple_times_row_to_row(1,0,1)
        if not (s[0] == p1 and
                s[1] == Plane(normal_vector=Vector([10,11,10]), constant_term=12) and
                s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
                s[3] == p3):
            print("Failed test case 8")
        else:
            print("Passed test case 8")

        s.add_multiple_times_row_to_row(-1,1,0)
        if not (s[0] == Plane(normal_vector=Vector([-10,-10,-10]), constant_term=-10) and
                s[1] == Plane(normal_vector=Vector([10,11,10]), constant_term=12) and
                s[2] == Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) and
                s[3] == p3):
            print("Failed test case 9")
        else:
            print("Passed test case 9")

    if test_triangular_form:
        print("\n=== Triangular Form Quiz ===\n")

        p1 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p2 = Plane(normal_vector=Vector([0,1,1]), constant_term=2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        if not (t[0] == p1 and
                t[1] == p2):
            print("Failed test case 1")
        else:
            print("Passed test case 1")

        p1 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p2 = Plane(normal_vector=Vector([1,1,1]), constant_term=2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        if not (t[0] == p1 and
                t[1] == Plane(constant_term=1)):
            print("Failed test case 2")
        else:
            print("Passed test case 2")

        p1 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p2 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
        p3 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
        p4 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)
        s = LinearSystem([p1,p2,p3,p4])
        t = s.compute_triangular_form()
        if not (t[0] == p1 and
                t[1] == p2 and
                t[2] == Plane(normal_vector=Vector([0,0,-2]), constant_term=2) and
                t[3] == Plane()):
            print("Failed test case 3")
        else:
            print("Passed test case 3")

        p1 = Plane(normal_vector=Vector([0,1,1]), constant_term=1)
        p2 = Plane(normal_vector=Vector([1,-1,1]), constant_term=2)
        p3 = Plane(normal_vector=Vector([1,2,-5]), constant_term=3)
        s = LinearSystem([p1,p2,p3])
        t = s.compute_triangular_form()
        if not (t[0] == Plane(normal_vector=Vector([1,-1,1]), constant_term=2) and
                t[1] == Plane(normal_vector=Vector([0,1,1]), constant_term=1) and
                t[2] == Plane(normal_vector=Vector([0,0,-9]), constant_term=-2)):
            print("Failed test case 4")
        else:
            print("Passed test case 4")


if __name__ == '__main__':
    main()
