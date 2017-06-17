#!/usr/local/bin/python3

def main():
    # X^2 - 1
    p_1 = (-1, 0, 1)
    r_1 = newton_raphson(p_1)
    print('Polynomial {} has root of {}'.format(print_poly(p_1), r_1))

    # X^3 - 27
    p_2 = (-27, 0, 0, 1)
    r_2 = newton_raphson(p_2)
    print('Polynomial {} has root of {}'.format(print_poly(p_2), r_2))


def print_poly(polynomial):
    '''
    Creates a string for a given polynomial, entered as a tuple of coefficients
    where the index i of the item represents the power of the variable x.
    '''
    if polynomial[0] == 0:
        output = ''
    else:
        output = str(polynomial[0])

    for i, a in enumerate(polynomial):
        if a == 0 or i == 0:
            continue
        output = str(a) + 'x^' + str(i) + ' + ' + output

    return output


def eval_polynomial(polynomial, x):
    '''
    Inputs a tuple of coefficients a_i where the index i of the item represents
    the power of the variable x. Evaluates and returns the polynomial for given
    value of x.
    '''
    result = 0
    for i, a in enumerate(polynomial):
        result += a * (x ** i)

    return result


def compute_derivative(polynomial):
    '''
    Inputs a tuple of coefficients a_i where the index i of the item represents
    the power of the variable x. Returns a tuple in similar form that represents
    the derivative of the given polynomial.
    '''
    derivative = []
    for a, i in enumerate(polynomial):
        derivative.append(i*a)

    return tuple(derivative[1:])


def newton_raphson(polynomial, epsilon=0.01):
    '''
    General approximation to find the roots of a polynomial in one variable.
    p(x) = a_n * x^n + a_n-1 * x^n-1 + ... + a_1 * x + a_0
    Find r such that p(r) = 0
    If g is an approximation of the root, then g - p(g)/p'(g) is a better
    approximation, where p' is the derivative of p.
    Input is tuple of coefficients a_i where the index i of the item represents the
    power of the variable x
    '''
    guess = 1
    derivative = compute_derivative(polynomial)
    p_of_guess = eval_polynomial(polynomial, guess)
    d_of_guess = eval_polynomial(derivative, guess)

    while abs(p_of_guess) > epsilon:
        guess = guess - (p_of_guess / d_of_guess)
        p_of_guess = eval_polynomial(polynomial, guess)
        d_of_guess = eval_polynomial(derivative, guess)

    return guess


if __name__ == '__main__':
    main()
