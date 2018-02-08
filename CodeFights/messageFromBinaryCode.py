#!/usr/local/bin/python
# Code Fights Message from Binary Code Problem


def messageFromBinaryCode(code):
    sz = 8
    return ''.join([chr(int(code[i:i + sz], 2)) for i in
                    range(0, len(code), sz)])


def main():
    tests = [
        ["010010000110010101101100011011000110111100100001", "Hello!"],
        ["01001101011000010111100100100000011101000110100001100101001000000100"
         "01100110111101110010011000110110010100100000011000100110010100100000"
         "0111011101101001011101000110100000100000011110010110111101110101",
         "May the Force be with you"],
        ["01011001011011110111010100100000011010000110000101100100001000000110"
         "11010110010100100000011000010111010000100000011000000110100001100101"
         "01101100011011000110111100101110",
         "You had me at `hello."]
    ]

    for t in tests:
        res = messageFromBinaryCode(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: messageFromBinaryCode({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: messageFromBinaryCode({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
