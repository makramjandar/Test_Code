#!/usr/local/bin/python
# Code Fights Sort by Height Problem


def sortByHeight(a):
    trees = [i for i, t in enumerate(a) if t == -1]
    humans = sorted([h for h in a if h != -1])
    for tree in trees:
        humans.insert(tree, -1)
    return humans


def main():
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    new = sortByHeight(a)
    print(new)


if __name__ == '__main__':
    main()
