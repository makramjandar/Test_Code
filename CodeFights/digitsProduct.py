#!/usr/local/bin/python
# Code Fights Digits Product Problem


def digitsProduct(product):
    ans = min([int(str(i) + str(product // i)) for i in
               range(1, round(product**0.5) + 1) if product % i == 0])
    if ans == product:
        return -1
    else:
        return ans


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
        [360, 589]
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
