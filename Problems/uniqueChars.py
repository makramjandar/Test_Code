#!/usr/local/bin/python3


def main():
    # Test suite
    strings = [None, '', 'Young Frankenstein', 'Yodeling cat']
    results = [False, True, False, True]
    for i, s in enumerate(strings):
        if has_unique_chars(s) == results[i]:
            print('PASSED test case: {} returned {}'.format(s, results[i]))
        else:
            print('FAILED test case: {} should return {}'.format(s, results[i]))

    return 0

def has_unique_chars(string):
    '''
    Determines if given string has unique characters (is case sensitive)
    Input: string
    Output: Boolean
    '''
    if string is None:
        return False

    char_set = set()
    for c in string:
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True


if __name__ == '__main__':
    main()
