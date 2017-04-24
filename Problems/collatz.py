#!/Applications/anaconda/envs/Python3/bin


def main():
    number = input("Enter a positive integer (negatives are converted): ")

    while True:
        try:
            number = abs(int(number))
            break
        except ValueError:
            number = input("Entry must be a number: ")

    sequence = collatz(number)

    while (sequence != 1):
        sequence = collatz(sequence)


def collatz(number):
    result = 1
    if number % 2 == 0:
        result = number // 2
        print(result)
    else:
        result = 3 * number + 1
        print(result)

    return result


if __name__ == '__main__':
    main()
