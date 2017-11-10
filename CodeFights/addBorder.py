#!/usr/local/bin/python
# Code Fights Add Border Problem


def addBorder(picture):
    picSize = len(picture[0]) + 2
    padding = '*' * picSize
    return [padding] + ['*' + row + '*' for row in picture] + [padding]


def main():
    test = ['abc', 'ded']
    print(addBorder(test))


if __name__ == '__main__':
    main()
