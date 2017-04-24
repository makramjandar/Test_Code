#!/Applications/anaconda/envs/Python3/bin
# Based on code created for Udacity Linear Algebra Refresher course


from vector import Vector


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0
        self.constant_term = constant_term

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]
            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += " = {}".format(constant)

        return output


    def is_parallel(self, l):
        # Takes another line, returns Boolean whether lines are parallel
        l1_normal_vector = self.normal_vector
        l2_normal_vector = l.normal_vector
        # Use Vector class is_parallel method to check normal vectors
        return l1_normal_vector.is_parallel(l2_normal_vector)


    def __eq__(self, l):
        # Takes another line, returns Boolean whether lines are same
        if self.normal_vector.is_zero():
            if not l.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - l.constant_term
                return Line.is_near_zero(diff)
        elif l.normal_vector.is_zero():
            return False

        if not self.is_parallel(l):
            return False

        new_line = self.basepoint - l.basepoint
        n = self.normal_vector

        return new_line.is_orthogonal(n)


    def intersection(self, l):
        # Takes another line, returns the intersection point
        if self == l:
            print("Same lines, infinite number of intersections")
            return None
        elif self.is_parallel(l):
            print("Parallel lines, no intersection points")
            return None
        else:
            A, B = self.normal_vector.coordinates
            C, D = l.normal_vector.coordinates
            k_1 = self.constant_term
            k_2 = l.constant_term
            #print("Intersection from A={} B={} C={} D={}".format(A, B, C, D))
            #print("Constants: k1={}, k2={}".format(k_1, k_2))
            denom = A*D - B*C
            x = (D*k_1 - B*k_2) / denom
            y = (-C*k_1 + A*k_2) / denom
            print("Lines intersect")
            return Vector([x, y])


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not Line.is_near_zero(item):
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    @staticmethod
    def is_near_zero(number, eps=1e-10):
        return abs(number) < eps
