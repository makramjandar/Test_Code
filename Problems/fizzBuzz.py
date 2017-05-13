#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    try:
        fizz_buzz(None)
    except TypeError:
        print('PASSED TypeError check')

    try:
        fizz_buzz(0)
    except ValueError:
        print('PASSED ValueError check')

    print('FizzBuzz 15:')
    fizz_buzz(15)

    return 0

def fizz_buzz(n):
    ''' Classic FizzBuzz implementation.
        Multiples of 3 => 'Fizz'
        Multiples of 5 => 'Buzz'
        Multiples of 3 and 5 => 'FizzBuzz'
    '''
    # Check input
    if type(n) is not int:
        raise TypeError
    if n <= 0:
        raise ValueError

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(str(i))

    return 0

if __name__ == '__main__':
    main()
