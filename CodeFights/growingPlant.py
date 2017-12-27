#!/usr/local/bin/python
# Code Fights Growing Plant Problem


def growingPlant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    else:
        return (desiredHeight // (upSpeed - downSpeed))


def main():
    tests = [
        [100, 10, 910, 10],
        [10, 9, 4, 1]
    ]

    for t in tests:
        res = growingPlant(t[0], t[1], t[2])
        ans = t[3]
        if ans == res:
            print("PASSED: growingPlant({}, {}, {}) returned {}"
                  .format(t[0], t[1], t[2], res))
        else:
            print(("FAILED: growingPlant({}, {}, {}) returned {},"
                   "answer: {}").format(t[0], t[1], t[2], res, ans))


if __name__ == '__main__':
    main()
