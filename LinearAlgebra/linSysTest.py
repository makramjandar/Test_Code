#!/usr/local/bin/Python3

from vector import Vector
from plane import Plane
from hyperplane import Hyperplane
from linsys import LinearSystem
from linsysHyper import LinearSystemHyper


def main():
    test_row_ops = False
    test_triangular_form = False
    test_rref = False
    test_ge_solution = False
    test_parametrization = False
    test_hyperplane = True

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

    # Test Triangular Form
    if test_triangular_form:
        print("\n=== Triangular Form Quiz ===\n")

        p4 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p5 = Plane(normal_vector=Vector([0,1,1]), constant_term=2)
        s1 = LinearSystem([p4, p5])
        t1 = s1.compute_triangular_form()
        if not (t1[0] == p4 and
                t1[1] == p5):
            print("Failed test case 1")
        else:
            print("Passed test case 1")

        p6 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p7 = Plane(normal_vector=Vector([1,1,1]), constant_term=2)
        s2 = LinearSystem([p6, p7])
        t2 = s2.compute_triangular_form()
        if not (t2[0] == p6 and
                t2[1] == Plane(constant_term=1)):
            print("Failed test case 2")
        else:
            print("Passed test case 2")

        p8 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p9 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
        p10 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
        p11 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)
        s3 = LinearSystem([p8, p9, p10, p11])
        t3 = s3.compute_triangular_form()
        if not (t3[0] == p8 and
                t3[1] == p9 and
                t3[2] == Plane(normal_vector=Vector([0,0,-2]), constant_term=2) and
                t3[3] == Plane()):
            print("Failed test case 3")
        else:
            print("Passed test case 3")

        p12 = Plane(normal_vector=Vector([0,1,1]), constant_term=1)
        p13 = Plane(normal_vector=Vector([1,-1,1]), constant_term=2)
        p14 = Plane(normal_vector=Vector([1,2,-5]), constant_term=3)
        s4 = LinearSystem([p12, p13, p14])
        t4 = s4.compute_triangular_form()
        if not (t[0] == Plane(normal_vector=Vector([1,-1,1]), constant_term=2) and
                t[1] == Plane(normal_vector=Vector([0,1,1]), constant_term=1) and
                t[2] == Plane(normal_vector=Vector([0,0,-9]), constant_term=-2)):
            print("Failed test case 4")
        else:
            print("Passed test case 4")

    # Test Reduced Row Echelon Form
    if test_rref:
        print("\n=== Reduced Row Echelon Form Quiz ===\n")

        p15 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p16 = Plane(normal_vector=Vector([0,1,1]), constant_term=2)
        s5 = LinearSystem([p15, p16])
        r1 = s5.compute_rref()
        if not (r1[0] == Plane(normal_vector=Vector([1,0,0]), constant_term=-1) and
                r1[1] == p16):
            print("Failed test case 1")
        else:
            print("Passed test case 1")

        p17 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p18 = Plane(normal_vector=Vector([1,1,1]), constant_term=2)
        s6 = LinearSystem([p17, p18])
        r2 = s6.compute_rref()
        if not (r2[0] == p17 and
                r2[1] == Plane(constant_term=1)):
            print("Failed test case 2")
        else:
            print("Passed test case 2")

        p19 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p20 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
        p21 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
        p22 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)
        s7 = LinearSystem([p19, p20, p21, p22])
        r3 = s7.compute_rref()
        if not (r3[0] == Plane(normal_vector=Vector([1,0,0]), constant_term=0) and
                r3[1] == p20 and
                r3[2] == Plane(normal_vector=Vector([0,0,-2]), constant_term=2) and
                r3[3] == Plane()):
            print("Failed test case 3")
        else:
            print("Passed test case 3")

        p23 = Plane(normal_vector=Vector([0,1,1]), constant_term=1)
        p24 = Plane(normal_vector=Vector([1,-1,1]), constant_term=2)
        p25 = Plane(normal_vector=Vector([1,2,-5]), constant_term=3)
        s8 = LinearSystem([p23, p24, p25])
        r4 = s8.compute_rref()
        if not (r4[0] == Plane(normal_vector=Vector([1,0,0]), constant_term=23/9) and
                r4[1] == Plane(normal_vector=Vector([0,1,0]), constant_term=7/9) and
                r4[2] == Plane(normal_vector=Vector([0,0,1]), constant_term=2/9)):
            print("Failed test case 4")
        else:
            print("Passed test case 4")

    # Test Gaussian Elimination solutions
    if test_ge_solution:
        print("\n=== Gaussian Elimination Solution Quiz ===\n")

        p26 = Plane(normal_vector=Vector([5.862,1.178,-10.366]), constant_term=-8.15)
        p27 = Plane(normal_vector=Vector([-2.931,-0.589,5.183]), constant_term=-4.075)
        s9 = LinearSystem([p26, p27])
        print(s9.do_gaussian_elimination())


        p28 = Plane(normal_vector=Vector([8.631,5.112,-1.816]), constant_term=-5.113)
        p29 = Plane(normal_vector=Vector([4.315,11.132,-5.27]), constant_term=-6.775)
        p30 = Plane(normal_vector=Vector([-2.158,3.01,-1.727]), constant_term=-0.831)
        s10 = LinearSystem([p28, p29, p30])
        print(s10.do_gaussian_elimination())


        p31 = Plane(normal_vector=Vector([5.262,2.739,-9.878]), constant_term=-3.441)
        p32 = Plane(normal_vector=Vector([5.111,6.358,7.638]), constant_term=-2.152)
        p33 = Plane(normal_vector=Vector([2.016,-9.924,-1.367]), constant_term=-9.278)
        p34 = Plane(normal_vector=Vector([2.167,-13.543,-18.883]), constant_term=-10.567)
        s11 = LinearSystem([p31, p32, p33, p34])
        print(s11.do_gaussian_elimination())

    # Test parametrization
    if test_parametrization:
        print("\n=== Parametrization Quiz ===\n")

        p35 = Plane(normal_vector=Vector([0.786,0.786,0.588]), constant_term=-0.714)
        p36 = Plane(normal_vector=Vector([-0.131,-0.131,0.244]), constant_term=0.319)
        s12 = LinearSystem([p35, p36])
        print(s12.compute_solution())

        p37 = Plane(normal_vector=Vector([8.631,5.112,-1.816]), constant_term=-5.113)
        p38 = Plane(normal_vector=Vector([4.315,11.132,-5.27]), constant_term=-6.775)
        p39 = Plane(normal_vector=Vector([-2.158,3.01,-1.727]), constant_term=-0.831)
        s13 = LinearSystem([p37, p38, p39])
        print(s13.compute_solution())

        p40 = Plane(normal_vector=Vector([0.935,1.76,-9.365]), constant_term=-9.955)
        p41 = Plane(normal_vector=Vector([0.187,0.352,-1.873]), constant_term=-1.991)
        p42 = Plane(normal_vector=Vector([0.374,0.704,-3.746]), constant_term=-3.982)
        p43 = Plane(normal_vector=Vector([-0.561,-1.056,5.619]), constant_term=5.973)
        s14 = LinearSystem([p40, p41, p42, p43])
        print(s14.compute_solution())

    # Test hyperplanes - created LInearSystemHyper to preserve tests above
    # file only changes the import statement at the top
    if test_hyperplane:
        print("\n=== Hyperplane Quiz ===\n")

        p44 = Hyperplane(normal_vector=Vector([0.786,0.786]), constant_term=-0.714)
        p45 = Hyperplane(normal_vector=Vector([-0.131,-0.131]), constant_term=0.319)
        s15 = LinearSystemHyper([p44, p45])
        print(s15.compute_solution())

        p46 = Hyperplane(normal_vector=Vector([2.102,7.489,-0.786]), constant_term=-5.113)
        p47 = Hyperplane(normal_vector=Vector([-1.131,-8.318,1.209]), constant_term=-6.775)
        p48 = Hyperplane(normal_vector=Vector([9.015,-5.873,1.105]), constant_term=0.831)
        s16 = LinearSystemHyper([p46, p47, p48])
        print(s16.compute_solution())

        p49 = Hyperplane(normal_vector=Vector([0.786, 0.786, 8.123, 1.111, -8.363]), constant_term=-9.955)
        p50 = Hyperplane(normal_vector=Vector([-0.131, -0.131, 7.05, -2.813, 1.19]), constant_term=-1.991)
        p51 = Hyperplane(normal_vector=Vector([9.015, -5.873, -1.105, 2.013, -2.802]), constant_term=-3.982)
        s17 = LinearSystemHyper([p49, p50, p51])
        print(s17.compute_solution())



if __name__ == '__main__':
    main()
