#!/Applications/anaconda/envs/Python3/bin

def main():
    # Get input from user and display it
    feels = input("On a scale of 1-10, how do you feel? ")
    print("You selected: {}".format(feels))

    # Python Data Types
    integer = 42
    floater = 3.14
    stringer = 'Hello, World!'
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
    num1, num2 = 0, 1
    if (num1 > num2):
        print("{} is greater than {}".format(num1, num2))
    elif (num1 < num2):
        print("{} is less than {}".format(num1, num2))
    else:
        print("{} is equal to {}".format(num1, num2))

    bigger = num1 if num1 >= num2 else num2
    smaller = num1 if num1 < num2 else num2
    print("Conditional statment says {} is greater than or equal to {}".format(bigger, smaller))

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

    print(choices)
    print("Option 1 was {} and returned: {}".format(opt1, choices.get(opt1, default)))
    print("Option 2 was {} and returned: {}".format(opt2, choices.get(opt2, default)))

    # Loops
    print("Fibonacci series up to 100:")
    a, b = 0, 1
    while b < 100:
        print(b, end=" ")
        a, b = b, a + b
    print()

    for letter in stringer:
        if letter in 'aeiouAEIOU':
            continue
        if letter in '!@#$%^&*.,?;:-_+=|':
            break
        print(letter)

    # Get an index using a for loop with enumerate()
    for index, letter in enumerate(stringer):
        print("Index: {} is letter: {}".format(index, letter))


if __name__ == '__main__':
    main()
