#!/usr/local/bin/python
# Think Like a Programmer Chapter 2: Pure Puzzles exercises


def main():
    test_pound_shapes = False
    test_base_conversion = True

    if test_pound_shapes:
        poundV()
        print()
        poundDiamond()

    if test_base_conversion:
        tests = [
            # [1, 1, 2, 1],  # ValueError test
            # ['G', 17, 10, 17],  # ValueError test
            # [15, 10, 10, '15'],
            # ['101', 2, 10, '5'],
            # ['1000', 2, 10, '8'],
            # ['A', 16, 10, '10'],
            # ['10', 16, 10, '16'],
            [11, 10, 16, 'B'],
            ['1100', 2, 16, 'C']
        ]

        for t in tests:
            print("Testing baseConversion({}, {}, {})"
                  .format(t[0], t[1], t[2]))
            try:
                res = baseConversion(t[0], t[1], t[2])
                if t[3] == res:
                    print("PASSED: baseConversion({}, {}, {}) returned {}"
                          .format(t[0], t[1], t[2], res))
                else:
                    print("FAILED: baseConversion({}, {}, {}) returned {}, "
                          "answer: {}".format(t[0], t[1], t[2], res, t[3]))
            except ValueError:
                print("PASSED: ValueError test")


def poundV():
    '''
    Using only single output statements of a space, pound, or new line, create:
    ########
     ######
      ####
       ##
    '''
    n = 4
    space = ' '
    pound = '#'
    for i in range(n, 0, -1):
        print((space * (n - i)) + (pound * i * 2) + (space * (n - i)))


def poundDiamond():
    '''
    Using only single output statements of a space, pound, or new line, create:
       ##
      ####
     ######
    ########
    ########
     ######
      ####
       ##
    '''
    n = 4
    space = ' '
    pound = '#'
    rangeItem = list(range(1, n + 1))

    for i in rangeItem + rangeItem[::-1]:
        print((space * (n - i)) + (pound * i * 2) + (space * (n - i)))


def baseConversion(num, s_base, t_base):
    '''
    Takes a number num as str or int. Converts it from the source base (s_base,
        an int) into the target base (t_base, an int) and returns new number
        as a string.
        Source and target bases must be between 2 and 16.
    Input: num (str), s_base (int), t_base (int)
    Output: str
    '''
    num = str(num)
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F']

    # Input checking
    if type(s_base) is not int or type(t_base) is not int:
        raise ValueError
    if (s_base < 2 or s_base > 16 or t_base < 2 or t_base > 16):
        raise ValueError

    # Convert number to base 10
    if s_base == 10:
        # print("Num in base 10 already: {}".format(num))
        base_10 = int(num)
    else:
        # print("Converting {} to base 10 from base {}".format(num, s_base))
        base_10 = sum([digits.index(ch) * (s_base ** i) for i, ch in
                       enumerate(list(num)[::-1])])
        # print("Num in base 10 is: {}".format(base_10))

    # Convert base-10 number to target base
    converted = ''
    if t_base == 10:
        converted = str(base_10)
    else:
        while base_10 > 0:
            r = base_10 % t_base
            converted = digits[r] + converted
            # print("Num: {}, num/{}: {}, digit: {}"
            #       .format(base_10, t_base, r, digits[r]))
            base_10 //= t_base

    return converted


if __name__ == '__main__':
    main()
