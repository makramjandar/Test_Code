#!/Applications/anaconda/envs/Python3/bin
# Based on code created for Udacity Linear Algebra Refresher course

from copy import deepcopy

from vector import Vector
from plane import Plane


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
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


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
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


    @staticmethod
    def is_near_zero(number, eps=1e-10):
        return abs(number) < eps



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
p0 = Plane(Vector([1, 0, 0]), 1)
p1 = Plane(Vector([0, 1, 0]), 2)
p2 = Plane(Vector([0, 0, 1]), 3)
s = LinearSystem([p0, p1, p2])

print(s.indices_of_first_nonzero_terms_in_each_row())
