#!/Applications/anaconda/envs/Python3/bin

import re

def main():
    '''Examples Using Regular Expressions in Python'''

    fh = open('sonnets.txt')
    # Use raw string for backslash, other special characters
    # Prints the Roman Numerals before each sonnet
    pattern = re.compile(r'[IVXLCDM]+\.')
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')


    return 0


if __name__ == '__main__':
    main()
