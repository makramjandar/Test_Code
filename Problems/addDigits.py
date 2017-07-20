#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        [-1, None], # Should throw a ValueError
        [0, 0],
        [9, 9],
        [138, 3],
        [65536, 7]
    ]

    print('Testing add_digits')
    for item in tests:
        try:
            temp_result = add_digits(item[0])
            if temp_result == item[1]:
                print('PASSED: add_digits({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: add_digits({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

        except ValueError:
            print('PASSED ValueError test')


    print('\nTesting add_digits_digital_root')
    for item in tests:
        try:
            temp_result = add_digits_digital_root(item[0])
            if temp_result == item[1]:
                print('PASSED: add_digits_digital_root({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: add_digits_digital_root({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

        except ValueError:
            print('PASSED ValueError test')

    return 0


def add_digits(val):
    '''
    Sums the digits of an integer until it reduces to one digit
    Input: val is non-negative integer
    Output: single digit integer
    Assumes no other data structure can be used
    '''
    # Check inputs
    if type(val) is not int:
        raise TypeError('Input must be an integer')

    if val < 0:
        raise ValueError('Input must be non-negative')

    digit_sum = val

    while digit_sum > 9:
        # Sum the digits in integer
        temp_sum = 0
        while digit_sum > 0:
            temp_sum += digit_sum % 10
            digit_sum = digit_sum // 10

        digit_sum = temp_sum

    return digit_sum


def add_digits_digital_root(val):
    '''
    This is a digital root, can be solved taking % 9
    Time: O(1)
    Complexity: O(1)
    '''
    # Check inputs
    if type(val) is not int:
        raise TypeError('Input must be an integer')

    if val < 0:
        raise ValueError('Input must be non-negative')

    if val == 0:
        return 0
    elif val % 9 == 0:
        return 9
    else:
        return val % 9


if __name__ == '__main__':
    main()
