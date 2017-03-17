#!/Applications/anaconda/envs/Python3/bin

def main():
    '''Examples Using Exceptions in Python'''
    # Python exceptions: http://docs.python.org/library/exceptions.html

    # Catch exceptions with try
    try:
        f = open('noFile.txt')
    except IOError as e:
        print('Oh no, IOError:', e)
    except ValueError as e:
        print('Oh no, ValueError:', e)
    else:
        # Can put the else code in the try part, too
        for line in f:
            print(line, end='')

    # Raise own exceptions
    try:
        for line in readDocFile('noFile.txt'):
            print(line.strip())
    except ValueError as e:
        print('Bad filename:', e)

    return 0


def readDocFile(filename):
    if filename.endswith('.doc'):
        f = open(filename)
        return f.readlines()
    else:
        raise ValueError('Filename must end with .doc')


if __name__ == '__main__':
    main()
