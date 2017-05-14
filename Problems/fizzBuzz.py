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

    test_fizz_buzz = [
        '1',
        '2',
        'Fizz',
        '4',
        'Buzz',
        'Fizz',
        '7',
        '8',
        'Fizz',
        'Buzz',
        '11',
        'Fizz',
        '13',
        '14',
        'FizzBuzz'
    ]

    result = fizz_buzz(15)
    # print('fizz_buzz(15): {}'.format(result))
    for i, n in enumerate(test_fizz_buzz):
        if n != result[i]:
            print('FAILED fizz_buzz test')
            return -1
    print('PASSED fizz_buzz test')

    return 0


def fizz_buzz(n):
    ''' Classic FizzBuzz implementation.
        Multiples of 3 => 'Fizz'
        Multiples of 5 => 'Buzz'
        Multiples of both 3 and 5 => 'FizzBuzz'
    '''
    # Check input
    if type(n) is not int:
        raise TypeError
    if n < 1:
        raise ValueError

    fizzy = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzy.append('FizzBuzz')
        elif i % 3 == 0:
            fizzy.append('Fizz')
        elif i % 5 == 0:
            fizzy.append('Buzz')
        else:
            fizzy.append(str(i))

    return fizzy

if __name__ == '__main__':
    main()
