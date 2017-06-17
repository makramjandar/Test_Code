#!/usr/local/bin/python3

import math

def main():
    # Test suite for strPermutations
    print("=====Test Suite - Find Permutations of String=====")
    print("(Assumes all characters in the string are unique)")

    testStrings = ["", "a", "ab", "abc", "abcd"]
    for string in testStrings:
        result = strPermutations(string)
        total = len(result)

        print("Permutations of: {}".format(string))
        print("Results: {}".format(result))
        print("Total permutations found: {}".format(total))

        numPermsToFind = math.factorial(len(string))

        if total == numPermsToFind:
            print("PASS! Permutations expected: {}, found: {}".format(numPermsToFind, total))
        else:
            print("FAIL! Permutations expected: {}, found: {}".format(numPermsToFind, total))


def strPermutations(string):
    '''
    string => list of strings that represent all permutations of str
    Assumes all characters in string are unique
    '''

    if len(string) <= 1:
        return [string]
    else:
        permsList = []
        lastChar = string[-1]
        shorter = string[:-1]
        shortPermsList = strPermutations(shorter)
        for perm in shortPermsList:
            # split shorter perm, insert lastChar at each index
            for i in range(len(perm)+1):
                pList = list(perm)
                pList.insert(i, lastChar)
                newPerm = ''.join(pList)
                permsList.append(newPerm)

        return permsList


if __name__ == '__main__':
    main()
