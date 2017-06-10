#!/Applications/anaconda/envs/Python3/bin

import math
import random

def main():
    # Test suite
    pi = math.pi

    # print('Pi: {}\n'.format(pi))

    print('Test 1')
    test_1 = throwNeedles(random.uniform)
    print('Pi: {0:0.4f}, Estimated pi: {1:0.4f}, difference: {2:0.4f}\n'.format(pi, test_1, test_1 - pi))

    print('Test 2')
    test_2 = throwNeedles(random.uniform)
    print('Pi: {0:0.4f}, Estimated pi: {1:0.4f}, difference: {2:0.4f}\n'.format(pi, test_2, test_2 - pi))

    print('Test 3')
    test_3 = throwNeedles(random.uniform)
    print('Pi: {0:0.4f}, Estimated pi: {1:0.4f}, difference: {2:0.4f}\n'.format(pi, test_3, test_3 - pi))

    return 0


def throwNeedles(fcn, numNeedles = 100000):
    inCircle = 0
    estimates = []
    for Needles in range(1, numNeedles + 1, 1):
        x = fcn(0, 1)
        y = fcn(0, 1)
        if (x*x + y*y) <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))


if __name__ == '__main__':
    main()
