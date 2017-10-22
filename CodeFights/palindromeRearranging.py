#!/usr/local/bin/python
# Code Fights Palindrome Rearranging Problem


def palindromeRearranging(inputString):
    from collections import Counter
    is_even_len = len(inputString) % 2 == 0
    letter_freq = Counter(inputString)
    odd_counts = sum([freq % 2 for char, freq in letter_freq.items()])
    return (is_even_len and odd_counts == 0) or (not is_even_len and odd_counts == 1)


def main():
    tests = [
        ["aabb", True],
        ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc", False],
        ["abbcabb", True],
        ["zyyzzzzz", True],
        ["z", True],
        ["zaa", True],
        ["abca", False]
    ]

    for t in tests:
        res = palindromeRearranging(t[0])
        if t[1] == res:
            print("PASSED: palindromeRearranging({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: palindromeRearranging({}) should have returned {}"
                  .format(t[0], t[1]))


if __name__ == '__main__':
    main()
