#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        [None, None, None], # Should throw a TypeError
        ['abcd', 'abcde', 'e'],
        ['aaabbcdd', 'abdbacade', 'e'],
        ['abdbacade', 'aaabbcdd', 'e']
    ]

    for item in tests:
        try:
            temp_result = find_diff(item[0], item[1])
            if temp_result[0] == item[2]:
                print('PASSED: find_diff({}, {}) returned {}'.format(item[0], item[1], temp_result))
            else:
                print('FAILED: find_diff({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

        except TypeError:
            print('PASSED TypeError test')

    return 0

    return


def find_diff(str1, str2):
    '''
    Finds the one additional character in str 2 vs. str1
    Input: two strings
    Output: char (one additional character in str2)
    Assumes str2 contains all characters from str1, with one additional one
    '''
    if str1 is None or str2 is None:
        raise TypeError

    shorter = str1 if len(str1) < len(str2) else str2
    longer = str1 if len(str1) >= len(str2) else str2

    result = set(longer) - set(shorter)
    return result.pop()


if __name__ == '__main__':
    main()
