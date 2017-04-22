#!/Applications/anaconda/envs/Python3/bin
# Based on code created for Udacity Linear Algebra Refresher course

import math


class Vector(object):

    SAME_DIMENSION_ERROR = "Vectors must be same dimension."
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Unable to normalize zero vector."
    CANNOT_FIND_ANGLE_BETWEEN_VECTORS = "Unable to find angle - at least one vector is Zero Vector."
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "Unable to calculate a unique parallel component."
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "Unable to calculate a unique orthogonal component."
    CAN_ONLY_CALCULATE_FOR_2D_OR_3D_VECTORS_MSG = "Function only defined for 2D and 3D vectors."

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be non-empty.")

        except TypeError:
            raise TypeError("The coordinates must be an iterable.")


    def __str__(self):
        # How Vector item should print
        return "Vector: {}".format(self.coordinates)


    def __eq__(self, v):
        # Redefines equality of vectors
        return self.coordinates == v.coordinates


    def __add__(self, v):
        # Redefines addition of vectors
        if v.dimension != self.dimension:
            raise ValueError(self.SAME_DIMENSION_ERROR)
        else:
            result = [x+y for x, y in zip(self.coordinates, v.coordinates)]
            # For loop implementation:
            # result = []
            # for i in range(self.dimension):
            #     result.append(self.coordinates[i] + v.coordinates[i])
            return Vector(result)


    def __sub__(self, v):
        # Redefines subtraction of vectors
        if v.dimension != self.dimension:
            raise ValueError(self.SAME_DIMENSION_ERROR)
        else:
            result = [x-y for x, y in zip(self.coordinates, v.coordinates)]
            # For loop implementation:
            # result = []
            # for i in range(self.dimension):
            #     result.append(self.coordinates[i] - v.coordinates[i])
            return Vector(result)


    def scale(self, c):
        # Returns new vector where each item in self is scaled by c
        scaled = [c*x for x in self.coordinates]
        return Vector(scaled)


    def magnitude(self):
        # Returns the length of self
        squares = [x**2 for x in self.coordinates]
        return math.sqrt(sum(squares))


    def normalization(self):
        # Returns the unit vector in same direction as self
        try:
            mag = self.magnitude()
            return self.scale(1.0 / mag)

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


    def dot_product(self, v):
        # Returns the inner or dot product of [a1, a2] and [b1, b2] => a1*b1 + a2*b2
        product = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(product)


    def angle(self, v, in_degrees=False):
        # Returns the angle between two vectors in either radians or degrees
        # math.acos() returns angle in radians
        # math.degrees(rad) converts angle in radians to degrees
        # math.radians(deg) converts angle in degrees to radians
        try:
            u1 = self.normalization()
            u2 = v.normalization()
            radians = math.acos(u1.dot_product(u2))
            if in_degrees:
                return math.degrees(radians)
            else:
                return radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_FIND_ANGLE_BETWEEN_VECTORS)
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        # Helper function to check if a vector is the Zero Vector
        return self.magnitude() < tolerance


    def is_parallel(self, v, tolerance=1e-10):
        # Returns Boolean whether vector v is parallel to self
        return ( self.is_zero() or
                v.is_zero() or
                self.angle(v) < tolerance or
                abs(self.angle(v) - math.pi) < tolerance )


    def is_orthogonal(self, v, tolerance=1e-10):
        # Returns Boolean whether vector v is orthogonol to self
        return (abs(self.dot_product(v)) < tolerance)


    def component_parallel_to(self, v):
        # Returns new vector that's the projection of v onto self vector
        try:
            unit = self.normalization()
            weight = v.dot_product(unit)
            return unit.scale(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def component_orthogonal_to(self, v):
        # Returns new vector that's the component of v orthogonal to self
        try:
            projection = self.component_parallel_to(v)
            return v - projection

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e


    def cross_product(self, v):
        # Returns new vector representing the cross product of self and v
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = v.coordinates
            cross = [   y1*z2 - y2*z1,
                      -(x1*z2 - x2*z1),
                        x1*y2 - x2*y1 ]
            return Vector(cross)

        except ValueError as e:
            msg = str(e)
            if msg == "not enough values to unpack (expected 3, got 2)":
                self_embedded_in_R3 = Vector(self.coordinates + (0.0,))
                v_embedded_in_R3 = Vector(v.coordinates + (0.0,))
                return self_embedded_in_R3.cross_product(v_embedded_in_R3)
            elif (msg == "too many values to unpack (expected 3)" or
                  msg == "not enough values to unpack (expected 3, got 1)"):
                raise Exception(self.CAN_ONLY_CALCULATE_FOR_2D_OR_3D_VECTORS_MSG)
            else:
                raise e

    def area_of_parallelogram_with(self, v):
        # Returns area of parallelogram spanned by self and v
        cross_vector = self.cross_product(v)
        return cross_vector.magnitude()


    def area_of_triangle_with(self, v):
        # Returns area of triangle spanned by self and v
        return 0.5 * self.area_of_parallelogram_with(v)
