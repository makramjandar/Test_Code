#!/usr/local/bin/python3


def main():
    # Test suite
    tests = [None, '', 'AABBCC', 'AAABCCDDDD']
    results = [None, '', 'AABBCC', 'A3BCCD4']

    for i in range(len(tests)):
        temp_result = compress_string(tests[i])
        if temp_result  == results[i]:
            print('PASS: {} returned {}'.format(tests[i], temp_result))
        else:
            print('FAIL: {} returned {}, should have returned {}'.format(tests[i], temp_result, results[i]))

    return 0

def compress_string(string):
    '''
    Compresses a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. Only compresses
    the string if it saves space ('AABBCC' stays same).
    Input: string
    Output: string
    '''
    if string is None:
        return None

    # Check length
    s_length = len(string)
    if s_length == 0:
        return string

    # Create compressed string
    compressed = []
    count = 1
    base_char = string[0]
    for i in range(1, s_length):
        # Current char is different than last one
        if string[i] != base_char:
            compressed.append(base_char)
            if count == 2:
                compressed.append(base_char)
            elif count > 2:
                compressed.append(str(count))
            # Change base_char to new character and reset count
            base_char = string[i]
            count = 1

        # Current char is same as last one
        else:
            count += 1

    # Append the last set of chars
    compressed.append(base_char)
    if count == 2:
        compressed.append(base_char)
    elif count > 2:
        compressed.append(str(count))

    if len(compressed) >= s_length:
        return string
    else:
        return ''.join(compressed)


if __name__ == '__main__':
    main()
