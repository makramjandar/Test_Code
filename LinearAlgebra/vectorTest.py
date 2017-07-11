#!/usr/local/bin/Python3

from vector import Vector


def main():
    test_operators = False
    test_mag_and_norm = False
    test_dot_and_angles = False
    test_parallel_orthogonal = False
    test_vector_projection = False
    test_cross_product = True
    test_errors = False # Includes examples to deliberately throw errors


    # Test addition, subtraction, and scalar multiplication of vectors
    if test_operators:
        print("\n=== Addition, Subtraction, and Scalar Multiplication Quiz ===\n")

        vec1 = Vector([8.218, -9.341])
        vec2 = Vector([-1.129, 2.111])
        print(vec1)
        print(vec2)
        print("Sum: {}\n".format(vec1+vec2))

        vec3 = Vector([7.119, 8.215])
        vec4 = Vector([-8.223, 0.878])
        print(vec3)
        print(vec4)
        print("Difference: {}\n".format(vec3-vec4))

        vec5 = Vector([1.671, -1.012, -0.318])
        c = 7.41
        print(vec5)
        print("Scaled by {}: {}\n".format(c, vec5.scale(c)))

    # Test magnitude and normalization of vectors
    if test_mag_and_norm:
        print("\n=== Magnitude and Normalization Quiz ===\n")

        vec6 = Vector([-0.221, 7.437])
        print(vec6)
        print("Magnitude: {}\n".format(vec6.magnitude()))

        vec7 = Vector([8.813, -1.331, -6.247])
        print(vec7)
        print("Magnitude: {}\n".format(vec7.magnitude()))

        vec8 = Vector([5.581, -2.136])
        print(vec8)
        print("Normalization: {}\n".format(vec8.normalization()))

        vec9 = Vector([1.996, 3.108, -4.554])
        print(vec9)
        print("Normalization: {}\n".format(vec9.normalization()))

        # Error test Zero Vector
        if test_errors:
            vec_zero = Vector([0, 0, 0])
            print(vec_zero)
            print("Normalization: {}\n".format(vec_zero.normalization()))

    # Test dot products and angles between vectors
    if test_dot_and_angles:
        print("\n=== Dot Products and Angles between Vectors Quiz ===\n")

        vec10 = Vector([7.887, 4.138])
        vec11 = Vector([-8.802, 6.776])
        print(vec10)
        print(vec11)
        print("Dot product: {}\n".format(vec10.dot_product(vec11)))

        vec12 = Vector([-5.955, -4.904, -1.874])
        vec13 = Vector([-4.496, -8.755, 7.103])
        print(vec12)
        print(vec13)
        print("Dot product: {}\n".format(vec12.dot_product(vec13)))

        vec14 = Vector([3.183, -7.627])
        vec15 = Vector([-2.668, 5.319])
        print(vec14)
        print(vec15)
        print("Angle (in radians): {}\n".format(vec14.angle(vec15)))

        vec16 = Vector([7.35, 0.221, 5.188])
        vec17 = Vector([2.751, 8.259, 3.985])
        print(vec16)
        print(vec17)
        print("Angle (in degrees): {}\n".format(vec16.angle(vec17, True)))

        # Not part of the quiz
        vec_a = Vector([2, 0])
        vec_b = Vector([0, 4])
        print(vec_a)
        print(vec_b)
        print("Dot product: {}".format(vec_a.dot_product(vec_b)))
        print("Angle (in radian): {}".format(vec_a.angle(vec_b)))
        print("Angle (in degrees): {}\n".format(vec_a.angle(vec_b, True)))

        if test_errors:
            vec_zero = Vector([0, 0, 0])
            print(vec16)
            print(vec_zero)
            print("Angle (in radians): {}\n".format(vec16.angle(vec_zero)))


    # Test Parallel and Orthogonal
    if test_parallel_orthogonal:
        print("\n=== Parallel and Orthogonal Quiz ===\n")

        vec18 = Vector([-7.579, -7.880])
        vec19 = Vector([22.737, 23.64])
        print(vec18)
        print(vec19)
        print("Parallel: {}".format(vec18.is_parallel(vec19)))
        print("Orthogonal: {}\n".format(vec18.is_orthogonal(vec19)))

        vec20 = Vector([-2.029, 9.970, 4.172])
        vec21 = Vector([-9.231, -6.639, -7.245])
        print(vec20)
        print(vec21)
        print("Parallel: {}".format(vec20.is_parallel(vec21)))
        print("Orthogonal: {}\n".format(vec20.is_orthogonal(vec21)))

        vec22 = Vector([-2.328, -7.284, -1.214])
        vec23 = Vector([-1.821, 1.072, -2.940])
        print(vec22)
        print(vec23)
        print("Parallel: {}".format(vec22.is_parallel(vec23)))
        print("Orthogonal: {}\n".format(vec22.is_orthogonal(vec23)))

        vec24 = Vector([2.118, 4.827])
        vec25 = Vector([0, 0])
        print(vec24)
        print(vec25)
        print("Parallel: {}".format(vec24.is_parallel(vec25)))
        print("Orthogonal: {}\n".format(vec24.is_orthogonal(vec25)))


    # Test Projection of Vectors and Component of Vector Orthogonal to b
    if test_vector_projection:
        print("\n=== Projection of Vectors Quiz ===\n")

        vec26 = Vector([3.039, 1.879])
        b1 = Vector([0.825, 2.036])
        print("V: {}".format(vec26))
        print("Basis: {}".format(b1))
        print("Projection of V onto Basis: {}\n".format(b1.component_parallel_to(vec26)))

        vec27 = Vector([-9.88, -3.264, -8.159])
        b2 = Vector([-2.155, -9.353, -9.473])
        print("V: {}".format(vec27))
        print("Basis: {}".format(b2))
        print("Component V orthogonal to Basis: {}\n".format(b2.component_orthogonal_to(vec27)))

        vec28 = Vector([3.009, -6.172, 3.692, -2.510])
        b3 = Vector([6.404, -9.144, 2.759, 8.718])
        print(vec28)
        print(b3)
        proj = b3.component_parallel_to(vec28)
        comp_orth = b3.component_orthogonal_to(vec28)
        print("Vparallel: {}".format(proj))
        print("Vorthogonal: {}".format(comp_orth))
        print("Vparallel + Vorthogonal: {}\n".format(proj + comp_orth))

    # Test Cross Product of Two 3D Vectors
    if test_cross_product:
        print("\n=== Cross Product of Two 3D Vectors Quiz ===\n")

        vec29 = Vector([8.462, 7.893, -8.187])
        vec30 = Vector([6.984, -5.975, 4.778])
        print(vec29)
        print(vec30)
        print("Cross product: {}\n".format(vec29.cross_product(vec30)))

        vec31 = Vector([-8.987, -9.838, 5.031])
        vec32 = Vector([-4.268, -1.861, -8.866])
        print(vec31)
        print(vec32)
        print("Area of parallelogram: {}".format(vec31.area_of_parallelogram_with(vec32)))
        print("Area of triangle: {}\n".format(vec31.area_of_triangle_with(vec32)))

        vec33 = Vector([1.500, 9.547, 3.691])
        vec34 = Vector([-6.007, 0.124, 5.772])
        print(vec33)
        print(vec34)
        print("Area of parallelogram: {}".format(vec33.area_of_parallelogram_with(vec34)))
        print("Area of triangle: {}\n".format(vec33.area_of_triangle_with(vec34)))

        if test_errors:
            vec35 = Vector([1.7, 2.3])
            vec36 = Vector([9.5, 8.4])
            print(vec35)
            print(vec36)
            print("Cross product: {}".format(vec35.cross_product(vec36)))
            print("Area of parallelogram: {}".format(vec35.area_of_parallelogram_with(vec36)))
            print("Area of triangle: {}\n".format(vec35.area_of_triangle_with(vec36)))

            vec37 = Vector([1.7])
            vec38 = Vector([4.6])
            print(vec37)
            print(vec38)
            print("Cross product: {}".format(vec37.cross_product(vec38)))
            print("Area of parallelogram: {}".format(vec37.area_of_parallelogram_with(vec38)))
            print("Area of triangle: {}\n".format(vec37.area_of_triangle_with(vec38)))



if __name__ == '__main__':
    main()
