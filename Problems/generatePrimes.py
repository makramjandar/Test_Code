#!/usr/local/bin/python3

import math

def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        [98.6, None], # Should throw a TypeError
        [20, [2, 3, 5, 7, 11, 13, 17, 19]]
    ]

    for item in tests:
        try:
            temp_result = generate_primes(item[0])
            if temp_result == item[1]:
                print('PASSED: generate_primes({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: generate_primes({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def generate_primes(max_num):
    '''
    Generates a list of prime numbers up to the given max number
    Input: int
    Output: list of ints
    '''
    if type(max_num) is not int:
        raise TypeError('Input must be an integer')

    primes = []

    if max_num <= 1:
        return primes

    primes.append(2)
    for n in range(3, max_num + 1, 2):
        primes.append(n) # assume it's prime
        square_root = math.ceil(math.sqrt(n))
        for d in range(2, square_root + 1):
            if n % d == 0:
                primes.pop() # Not prime, remove
                break

    return primes


if __name__ == '__main__':
    main()
