#!/usr/local/bin/python3


def main():
    for i in range(1, 8):
        print("============================")
        print("Towers of Hanoi: {} Disks".format(i))
        towers_of_hanoi(i)
        print("Number of moves: {}".format(2**i - 1))
        print("============================")

    return 0


def towers_of_hanoi(n, s="source", t="target", b="buffer"):
    # n is number of disks, smaller disk must always be on top of larger one
    assert n > 0

    if n == 1:
        print("Move {} to {}".format(s, t))
        return
    else:
        # Recursively move n-1 disks from source to buffer
        towers_of_hanoi(n-1, s, b, t)
        # Move largest disk from source to target
        towers_of_hanoi(1, s, t, b)
        # Recursively move n-1 disks from buffer to target
        towers_of_hanoi(n-1, b, t, s)


if __name__ == '__main__':
    main()
