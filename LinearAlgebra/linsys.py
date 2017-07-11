#!/usr/local/bin/Python3
# Based on code created for Udacity Linear Algebra Refresher course

from copy import deepcopy

from vector import Vector
from plane import Plane


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = ('All planes in the system should live in the same dimension')
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = "Linear System:\n"
        temp = ["Equation {}: {}".format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


    def swap_rows(self, row1, row2):
        # Switch the order of two rows in the linear system
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        orig_plane = self.planes[row]
        orig_n = orig_plane.normal_vector
        orig_k = orig_plane.constant_term

        new_n = orig_n.scale(coefficient)
        new_k = coefficient * orig_k
        self.planes[row] = Plane(normal_vector=new_n, constant_term=new_k)


    def add_multiple_times_row_to_row(self, coefficient, row_to_add,
                                      row_to_be_added_to):
        # Multiplies a row by a coefficient and adds it to other row
        # Get row_to_add normal vector and constant, multiply by coefficient
        rta = self.planes[row_to_add]
        rta_scaled_n = rta.normal_vector.scale(coefficient)
        rta_scaled_k = rta.constant_term * coefficient

        # Get normal vector and constant for row that's changing
        rtbat = self.planes[row_to_be_added_to]
        rtbat_n = rtbat.normal_vector
        rtbat_k = rtbat.constant_term

        # Add normal vectors and constant terms, set row to new plane
        new_n = rta_scaled_n + rtbat_n
        new_k = rta_scaled_k + rtbat_k

        self.planes[row_to_be_added_to] = Plane(normal_vector=new_n, constant_term=new_k)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def compute_triangular_form(self):
        system = deepcopy(self)
        first_nonzero_terms = system.indices_of_first_nonzero_terms_in_each_row()
        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                # Get the jth coefficient in equation i
                c = system.planes[i].normal_vector.coordinates[j]
                if LinearSystem.is_near_zero(c):
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue

                system.clear_coefficients_below(i, j)
                j += 1
                break

        return system


    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        num_equations = len(self)

        for k in range(row+1, num_equations):
            coefficient = self.planes[k].normal_vector.coordinates[col]
            if not LinearSystem.is_near_zero(coefficient):
                self.swap_rows(row, k)
                return True

        return False


    def clear_coefficients_below(self, row, col):
        num_equations = len(self)
        beta = self.planes[row].normal_vector.coordinates[col]

        for k in range(row+1, num_equations):
            n = self[k].normal_vector.coordinates
            gamma = n[col]
            alpha = -gamma / beta
            self.add_multiple_times_row_to_row(alpha, row, k)


    def clear_coefficients_above(self, row, col):
        for k in range(row)[::-1]:
            n = self[k].normal_vector.coordinates
            alpha = -(n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)


    def compute_rref(self):
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(num_equations)[::-1]:
            j = pivot_indices[i]
            if j < 0:
                continue
            tf.scale_row_to_make_coefficient_equal_one(i, j)
            tf.clear_coefficients_above(i, j)

        return tf


    def scale_row_to_make_coefficient_equal_one(self, row, col):
        n = self[row].normal_vector.coordinates
        beta = 1.0 / n[col]
        self.multiply_coefficient_and_row(beta, row)


    def do_gaussian_elimination(self):
        rref = self.compute_rref()

        try:
            rref.raise_exception_if_contradictory_equation()
            rref.raise_exception_if_too_few_pivots()
        except Exception as e:
            return str(e)

        num_variables = rref.dimension
        solution_coordinates = [rref.planes[i].constant_term for i in
                                range(num_variables)]

        return Vector(solution_coordinates)


    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector)

            except Exception as e:
                if str(e) == "No nonzero elements found":
                    constant_term = p.constant_term
                    if not LinearSystem.is_near_zero(constant_term):
                        raise Exception(self.NO_SOLUTIONS_MSG)

                else:
                    raise e


    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_variables = self.dimension

        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)


    def compute_solution(self):
        try:
            return self.do_gaussian_elimination_and_parametrization()

        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return str(e)
            else:
                raise e


    def do_gaussian_elimination_and_parametrization(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()

        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()

        return Parametrization(basepoint, direction_vectors)


    def extract_direction_vectors_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)

        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var]

            direction_vectors.append(Vector(vector_coords))

        return direction_vectors


    def extract_basepoint_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * num_variables

        for i, p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = p.constant_term

        return Vector(basepoint_coords)


    @staticmethod
    def is_near_zero(number, eps=1e-10):
        return abs(number) < eps



class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = (
        "The basepoint and direction vectors must live in the same dimension")

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):

        output = ''
        for coord in range(self.dimension):
            output += 'x_{} = {} '.format(coord + 1,
                                          round(self.basepoint.coordinates[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += '+ {} t_{}'.format(round(vector.coordinates[coord], 3),
                                             free_var + 1)
            output += '\n'
        return output




# p0 = Plane(Vector([1,1,1]), 1)
# p1 = Plane(Vector([0,1,0]), 2)
# p2 = Plane(Vector([1,1,-1]), 3)
# p3 = Plane(Vector([1,0,-2]), 2)
#
# s = LinearSystem([p0,p1,p2,p3])
#
# print(s.indices_of_first_nonzero_terms_in_each_row())
# print("{},{},{},{}".format(s[0],s[1],s[2],s[3]))
# print(len(s))
# print(s)
#
# s[0] = p1
# print(s)

# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()
