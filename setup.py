#!/Applications/anaconda/envs/Python3/bin

import sys

def main():
    '''Python 3 Quick Start Code Examples'''

    # Get input from user and display it
    # feels = input("On a scale of 1-10, how do you feel? ")
    # print("You selected: {}".format(feels))

    # Python Data Types
    integer = 42
    floater = 3.14
    stringer = 'Hello, World!'
    noner = None # singleton value, check: if var is None
    tupler = (1, 2, 3)
    lister = [1, 2, 3]
    dicter = dict(
        one = 1,
        two = 2,
        three = 3
    )
    boolTrue = True
    boolFalse = False

    # Conditionals
    print("=========== Conditionals ==========")
    num1, num2 = 0, 1
    if (num1 > num2):
        # print("{} is greater than {}".format(num1, num2))
        pass
    elif (num1 < num2):
        # print("{} is less than {}".format(num1, num2))
        pass
    else:
        # print("{} is equal to {}".format(num1, num2))
        pass

    # Python version of ternary operator
    bigger = num1 if num1 >= num2 else num2
    smaller = num1 if num1 < num2 else num2
    # print("Conditional statment says {} is greater than or equal to {}".format(bigger, smaller))

    # Python version of a switch statement
    choices = dict(
        a = 'First',
        b = 'Second',
        c = 'Third',
        d = 'Fourth',
        e = 'Fifth'
    )
    opt1 = 'c'
    opt2 = 'f'
    default = 'Option not found'

    # print("Python 'switch' statment using a dict: {}".format(choices))
    # print("Option 1 was {} and returned: {}".format(opt1, choices.get(opt1, default)))
    # print("Option 2 was {} and returned: {}".format(opt2, choices.get(opt2, default)))
    print("==============================")

    # Loops
    print("=========== Loops ==========")
    print("Fibonacci series up to 100:")
    a, b = 0, 1
    while b < 100:
        print(b, end=" ")
        a, b = b, a + b
    print()

    # print("For loop printing parts of {}".format(stringer))
    for letter in stringer:
        # Don't print the vowels
        if letter in 'aeiouAEIOU':
            continue
        # Stop looping at punctuation
        if letter in '!@#$%^&*.,?;:-_+=|':
            break
        # print(letter, end=" ")
    # print()
    print("==============================")

    # Get an index using a for loop with enumerate()
    # for index, letter in enumerate(stringer):
        # print("Index: {} is letter: {}".format(index, letter))


    # List comprehensions
    print("=========== List Comprehensions ==========")
    # Create a new list - [expression for variable in list]
    listOne = [0, 1, 2, 3, 4, 5]
    listSquares = [x*x for x in listOne]
    print("List comprehension: {}".format(listSquares))

    # Filter a list - [expression for variable in list if condition]
    listOdd = [x for x in listSquares if x % 2 == 1]
    print("Filtered list comprehension: {}".format(listOdd))

    # Dictionary comprehensions
    print("=========== Dict Comprehensions ==========")
    dictComp = {chr(64+x): x for x in range(1, 27)}
    print("Dict comprehension: {}".format(dictComp))

    # Set comprehension
    print("=========== Set Comprehensions ==========")
    setComp = {x**5 for x in range(2,8)}
    print("Set comprehension: {}".format(setComp))
    print("==============================")

    # Check if a type is an iterable
    print("=========== Is X Type Interable? ==========")
    print("Is a string an iterable? {}".format(hasattr(str, '__iter__')))
    print("Is a Boolean an iterable? {}".format(hasattr(bool, '__iter__')))
    print("Is a list an iterable? {}".format(hasattr(list, '__iter__')))
    print("Is a set an iterable? {}".format(hasattr(set, '__iter__')))
    print("Is an int an iterable? {}".format(hasattr(int, '__iter__')))
    print("==============================")

    # Generator Expressions
    # Similar to list comprehension, less space in memory
    print("=========== Generator Expressions ==========")
    genExp = (x**5 for x in range(2,8))
    listComp = [x**5 for x in range(2,8)]
    print("Type of a generator expression: {}".format(type(genExp)))
    print("Actual generator expression: {}".format(genExp))
    print("Size of generator expression: {}".format(sys.getsizeof(genExp)))
    print("Size of same list comprehension: {}".format(sys.getsizeof(listComp)))
    print("==============================")

    return 0

if __name__ == '__main__':
    main()
