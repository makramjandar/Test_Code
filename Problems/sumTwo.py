#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        [5, 7, 12],
        [-5, -7, -12],
        [5, -7, -2]
    ]

    for item in tests:
        try:
            temp_result = sum_two(item[0], item[1])
            if temp_result == item[2]:
                print('PASSED: sum_two({}, {}) returned {}'.format(item[0], item[1], temp_result))
            else:
                print('FAILED: sum_two({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def sum_two(a, b):
    '''
    Returns the sum of two integers without using the + or - operators
    Input: a, b both integers
    Output: integer
    '''
    if type(a) is not int or type(b) is not int:
        raise TypeError('a and b must be integers')

    result = a ^ b
    borrow = (a & b) << 1
    if borrow != 0:
        return sum_two(result, borrow)
    else:
        return result


if __name__ == '__main__':
    main()
