#!/Applications/anaconda/envs/Python3/bin

def main():
    '''Bitwise Operators and Examples'''

    x, y, allOn = 0x55, 0xaa, 0xff

    print("x is: ", end="")
    bitPrint(x)
    print("y is: ", end="")
    bitPrint(y)
    print("allOn is: ", end="")
    bitPrint(allOn)

    # Bitwise OR: |
    print("x | y: ", end="")
    bitPrint(x | y)

    # Bitwise AND: &
    print("x & y: ", end="")
    bitPrint(x & y)

    # Bitwise XOR: ^
    print("x ^ allOn: ", end="")
    bitPrint(x ^ allOn)

    # Bitwise Left Shift: <<
    print("allOn << 4: ", end="")
    bitPrint(allOn << 4)

    # Bitwise Right Shift: >>
    print("allOn >> 4: ", end="")
    bitPrint(allOn >> 4)

    # Bitwise One's Complement: ~
    print("One's complement of x (~x): ", end="")
    bitPrint(~x)

    return 0


def bitPrint(n):
    '''Prints a given number n in binary format to 8 places'''
    print('{:08b}'.format(n))

if __name__ == '__main__':
    main()
