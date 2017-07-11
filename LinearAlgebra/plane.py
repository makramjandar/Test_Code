#!/usr/local/bin/Python3
# Based on code created for Udacity Linear Algebra Refresher course

from vector import Vector


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = "No nonzero elements found"

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

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

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
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
            initial_index = Plane.first_nonzero_index(n)
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
        output += ' = {}'.format(constant)

        return output


    def is_parallel(self, p):
        # Takes another plane, returns Boolean whether planes are parallel
        # Use Vector class is_parallel method to check normal vectors
        return self.normal_vector.is_parallel(p.normal_vector)


    def __eq__(self, p):
        # Takes another plane, returns Boolean whether planes are same
        if self.normal_vector.is_zero():
            if not p.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - p.constant_term
                return Plane.is_near_zero(diff)
        elif p.normal_vector.is_zero():
            return False

        if not self.is_parallel(p):
            return False

        new_vector = self.basepoint - p.basepoint
        n = self.normal_vector

        return new_vector.is_orthogonal(n)


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not Plane.is_near_zero(item):
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    @staticmethod
    def is_near_zero(number, eps=1e-10):
        return abs(number) < eps
