#!/usr/local/bin/python
# Code Fights Digits Product Problem


def digitsProduct(product):
    def get_single_dig_factors(product):
        # Helper function to generate single-digit factors of product
        n = product
        factors = []
        for i in range(9, 1, -1):
            while n % i == 0 and n > 1:
                factors.append(i)
                n /= i
        if n > 9:
            # At least one factor is a two-digit prime number
            return None
        return sorted(factors)

    if product == 0:
        return 10
    elif product < 10:
        return product

    factors = get_single_dig_factors(product)
    if factors:
        return int(''.join([str(i) for i in factors]))
    else:
        return -1


def main():
    tests = [
        [12, 26],
        [19, -1],
        [450, 2559],
        [0, 10],
        [13, -1],
        [1, 1],
        [243, 399],
        [576, 889],
        [360, 589],
        [24, 38],
        [120, 358],
        [168, 378],
        [192, 388],
        [216, 389],
        [600, 3558],
        [33, -1],
        [81, 99]
    ]

    for t in tests:
        res = digitsProduct(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: digitsProduct({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: digitsProduct({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
