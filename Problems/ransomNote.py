#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        [None, None, None], # Should throw a TypeError
        ['', '', True],
        ['a', 'b', False],
        ['aa', 'ab', False],
        ['aa', 'aab', True]
    ]

    for item in tests:
        try:
            temp_result = match_note_to_magazine(item[0], item[1])
            if temp_result == item[2]:
                print('PASSED: match_note_to_magazine({}, {}) returned {}'.format(item[0], item[1], temp_result))
            else:
                print('FAILED: match_note_to_magazine({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def match_note_to_magazine(ransom_note, magazine):
    '''
    Takes a set of letters needed for a ransom note and determines if it can
    be created with the letters in the magazine
    Input: both ransom_note and magazine are strings
    Output: Boolean
    '''
    if type(ransom_note) is not str or type(magazine) is not str:
        raise TypeError('Inputs must be strings')

    # Empty string and longer ransom notes vs magazine cases
    if not ransom_note:
        return True
    elif not magazine or len(ransom_note) > len(magazine):
        return False

    freq_dict = {}

    for c in magazine:
        try:
            freq_dict[c] += 1
        except KeyError:
            freq_dict[c] = 1

    for l in ransom_note:
        try:
            freq_dict[l] -= 1
        except KeyError:
            return False
        if freq_dict[l] < 0:
            return False

    return True


if __name__ == '__main__':
    main()
