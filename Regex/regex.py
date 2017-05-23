#!/Applications/anaconda/envs/Python3/bin

import re

def main():
    '''Examples Using Regular Expressions in Python'''

    printRomanNumerals('sonnets.txt')
    replaceWord('sonnets.txt', 'beauty', 'vomit')
    #replaceWord('sonnets.txt', 'love', 'shart')

    return 0


def printRomanNumerals(filename):
    '''Reads filename data and prints Roman Numerals followed by .'''

    fh = open(filename, 'r')
    # Use raw string for backslash, other special characters
    # To access capturing groups: match.group(0) = full match
    # match.group(1) first captured group, etc.
    pattern = re.compile(r'[IVXLCDM]+\.')
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(match.group())


    fh.close()
    return 0


def replaceWord(filename, original, new):
    '''Prints any line with original word in it replaced with new word'''

    print('\nTime to replace the word {} with {} and print the improved line.\n'.format(original, new))

    fh = open(filename, 'r')
    pattern = re.compile(original)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub(new, line), end='')
            #print(re.sub(pattern, new, line), end='')

    fh.close()
    return 0


if __name__ == '__main__':
    main()
