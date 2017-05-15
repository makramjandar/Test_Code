#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        [None, 'foo', False],
        ['', 'foo', False],
        ['', '', True],
        ['foobarbaz', 'barbazfoo', True],
        ['foobrabaz', 'barbazfoo', False]
    ]

    for item in tests:
        temp_result = is_rotation(item[0], item[1])
        if temp_result == item[2]:
            print('PASSED: is_rotation({}, {}) returned {}'.format(item[0], item[1], temp_result))
        else:
            print('FAILED: is_rotation({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

    return 0


def is_substring(s1, s2):
    ''' Determines if s1 is a substring of s2, returns a Boolean '''
    if s1 is None or s2 is None:
        return False

    # Substrings can't be longer than the string
    if len(s1) > len(s2):
        return False

    return s1 in s2


def is_rotation(s1, s2):
    ''' Determines if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring. Returns a Boolean '''
    if s1 is None or s2 is None:
        return False

    if len(s1) == len(s2) and is_substring(s1, s2 + s2):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
