#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [
        [None, None], # Should throw a TypeError
        ['Here is a sample.', 'Here%20is%20a%20sample.'],
        ['Next one!', 'Next%20one!']
    ]

    for item in tests:
        try:
            temp_result = spaces_to_percent_twenty(item[0])
            if temp_result == item[1]:
                print('PASSED: spaces_to_percent_twenty({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: spaces_to_percent_twenty({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def spaces_to_percent_twenty(s):
    '''
    Replaces spaces in a string with %20, without using .replace method
    Input: string
    Output: string
    '''
    # Input checks
    if type(s) is not str:
        raise TypeError('Input must be a string')

    return ''.join([char if char != ' ' else '%20' for char in s])



if __name__ == '__main__':
    main()
