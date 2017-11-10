#!//urs/local/bin/python
# Code Fights Avoid Obstacles Problem


def avoidObstacles(inputArray):
    for jump in range(2, 40):
        safe = True
        for item in inputArray:
            if item % jump == 0:
                safe = False
                break
        if safe:
            return jump


def main():
    tests = [
        [[5, 3, 6, 7, 9], 4],
        [[2, 3], 4],
        [[1, 4, 10, 6, 2], 7]
    ]

    for t in tests:
        res = avoidObstacles(t[0])
        if t[1] == res:
            print("PASSED: avoidObstacles({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: avoidObstacles({}) returned {}, answer: {}"
                  .format(t[0], res, t[1]))


if __name__ == '__main__':
    main()
