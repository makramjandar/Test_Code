#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [ None, [''], ['f','o','o',' ','b','a','r']]
    for t in tests:
        print('Testing: {}'.format(t))
        print('Result: {}'.format(reverse_string_in_place(t)))

    return 0


def reverse_string_in_place(chars):
    ''' Reverses a string (input as a list of chars) in place '''
    if chars is None:
        return None
    for i in range(len(chars) // 2):
        chars[i], chars[-i-1] = chars[-i-1], chars[i]
    return chars

if __name__ == '__main__':
    main()
