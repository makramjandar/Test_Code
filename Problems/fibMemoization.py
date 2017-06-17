#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        [4, 3],
        [7, 13]
    ]

    for item in tests:
        try:
            temp_result = fib_memoization(item[0])
            if temp_result == item[1]:
                print('PASSED: fib_memoization({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: fib_memoization({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def fib_memoization(n, d={1:1, 2:1}):
    '''
    Calculates the nth Fibonacci number
    Input: n is integer, d is dict of previously calculated Fibonacci numbers
    Output: integer, the nth Fibonacci number
    '''
    # Input checks
    if type(n) is not int or type(d) is not dict:
        raise TypeError('n must be an integer, d must be a dictionary')


    if n in d:
        return d[n]
    else:
        result = fib_memoization(n-1, d) + fib_memoization(n-2, d)
        d[n] = result
        return result



if __name__ == '__main__':
    main()
