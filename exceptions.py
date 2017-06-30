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
        # Runs when try body completes with no exceptions
        for line in f:
            print(line, end='')
    finally:
        # Always executed after try, except, and else even if exceptions raised
        # or hit break/continue/return statement. Good for clean-up
        # f.close()
        pass

    # Exceptions in a while loop
    while True:
        try:
            n = input('Please enter an integer: ')
            n = int(n)
            break
        except ValueError:
            print('Input not an integer, please try again: ')
    print('Correct input!')

    # Raise own exceptions
    try:
        for line in readDocFile('noFile.txt'):
            print(line.strip())
    except ValueError as e:
        print('Bad filename:', e)

    testBool = True
    if testBool:
        raise CustomException('NOOOOOO!')


    # Assert that input is correct
    grades = [79, 92, 84]
    assert not len(grades) == 0, 'no grades data'

    return 0


def readDocFile(filename):
    if filename.endswith('.doc'):
        f = open(filename)
        return f.readlines()
    else:
        raise ValueError('Filename must end with .doc')


class CustomException(Exception):
    def __init__(self, error):
        super(Exception, self).__init__(error)
        print(error)



if __name__ == '__main__':
    main()
