def shapeArea(n):
    if n < 1 or n > 10**4:
        raise ValueError
    if n == 1:
        return 1
    else:
        innerArea = shapeArea(n - 1)
        return innerArea + (n - 1) * 4


def main():
    tests = [-1, 10**5, 1, 2, 3, 4]
    results = [False, False, 1, 5, 13, 25]
    for i, t in enumerate(tests):
        try:
            r = shapeArea(t)
            if r == results[i]:
                print("PASSED: shapeArea({}) returned {}".format(t, r))
            else:
                print("FAILED: shapeArea({}) returned\
                 {}, vs {}".format(t, r, results[i]))
        except ValueError:
            print("PASSED ValueError test")


if __name__ == '__main__':
    main()
