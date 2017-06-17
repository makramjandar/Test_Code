#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        [7, 5, 2],
        [-5, -7, 2],
        [-5, 7, -12],
        [5, -7, 12]
    ]

    for item in tests:
        try:
            temp_result = sub_two(item[0], item[1])
            if temp_result == item[2]:
                print('PASSED: sub_two({}, {}) returned {}'.format(item[0], item[1], temp_result))
            else:
                print('FAILED: sub_two({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def sub_two(a, b):
    '''
    Returns the difference of two integers without using the + or - operators
    Input: a, b both integers
    Output: integer
    '''
    if type(a) is not int or type(b) is not int:
        raise TypeError('a and b must be integers')

    # print('Calculating {} - {}'.format(a, b))
    # print('a: {:08b}, b: {:08b}'.format(a, b))
    result = a ^ b
    # print('Result a ^ b: {}, {:08b}'.format(result, result))
    borrow = (~a & b) << 1
    # print('Borrow: {}, {:08b}'.format(borrow, borrow))
    if borrow != 0:
        return sub_two(result, borrow)
    else:
        # print('Returning result: {}'.format(result))
        return result


if __name__ == '__main__':
    main()
