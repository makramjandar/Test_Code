#!/usr/local/bin/python
# Code Fights Line Encoding Problem


def lineEncoding(s):
    compressed_string = list()
    count = 0
    last_char = s[0]
    for char in s:
        if char == last_char:
            count += 1
        else:
            if count > 1:
                compressed_string.append(str(count))
                compressed_string.append(last_char)
                count = 1
                last_char = char
            else:
                # count is 1
                compressed_string.append(last_char)
                count = 1
                last_char = char
    if count > 1:
        compressed_string.append(str(count))

    compressed_string.append(last_char)

    return ''.join(compressed_string)


def main():
    tests = [
        ["aabbbc", "2a3bc"],
        ["abbcabb", "a2bca2b"],
        ["abcd", "abcd"]
    ]

    for t in tests:
        res = lineEncoding(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: lineEncoding({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: lineEncoding({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
