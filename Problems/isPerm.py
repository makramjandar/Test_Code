#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        [None, 'foo', False],
        ['', 'foo', False],
        ['Nib', 'bin', False],
        ['act', 'cat', True],
        ['a ct', 'ca t', True]
    ]

    for item in tests:
        temp_result = is_permutation(item[0], item[1])
        if temp_result == item[2]:
            print('PASSED: is_permutation({}, {}) returned {}'.format(item[0], item[1], temp_result))
        else:
            print('FAILED: is_permutation({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

    return 0


def is_permutation(str1, str2):
    '''
    Determines if string is a permutation of another
    Input: two strings
    Output: Boolean
    Assumes case and white space matter. Empty strings return False
    '''
    # Check input
    if str1 is None or str2 is None:
        return False

    if not str1 or not str2:
        return False

    # Check lengths
    if len(str1) != len(str2):
        return False

    char_dict = {}

    # Build character frequency dictionary for first string
    for c in str1:
        try:
            char_dict[c] += 1
        except KeyError:
            char_dict[c] = 1

    # Check characters in second string against character dictionary
    for c in str2:
        try:
            char_dict[c] -= 1
            if char_dict[c] < 0:
                return False
        except KeyError:
            return False

    return True


if __name__ == '__main__':
    main()
