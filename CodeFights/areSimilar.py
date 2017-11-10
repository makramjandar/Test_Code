#!/usr/local/bin/python
# Code Fights Are Similar Problem


def areSimilar(a, b):
    if a == b:
        return True

    for i in range(len(a)):
        if a[i] != b[i]:
            # Check that the item exists in the rest of the other list
            if (a[i] not in b[i:] or b[i] not in a[i:]):
                return False
            else:
                # Get indices for all matches, for each index, make swap in b,
                # check if new b matches a: yes => True, no => False
                b_front = b[:i]
                b_back = b[i:]
                indices = [j for j, item in enumerate(b_back) if item == a[i]]
                for k in indices:
                    b_back = b[i:]  # Reset back part of b
                    b_back[0], b_back[k] = b_back[k], b_back[0]
                    if a == b_front + b_back:
                        # Found a single swap that works
                        return True
                return False


def areSimilarRec(a, b):
    if a == b or len(a) < 1:
        return True

    if a[0] == b[0]:
        return areSimilarRec(a[1:], b[1:])
    else:
        # Check that the item exists in the other list
        if (a[0] not in b or b[0] not in a):
            return False
        else:
            # Get indices for all matches, for each index, make swap in b,
            # check if new b matches a: yes => return True, no => return False
            indices = [j for j, item in enumerate(b) if item == a[0]]
            for i in indices:
                temp_b = b[:]  # Reset temp_b
                temp_b[0], temp_b[i] = temp_b[i], temp_b[0]
                if a == temp_b:
                    return True
            return False


def main():
    tests = [
        [[1, 2, 3], [1, 2, 3], True],
        [[1, 2, 3], [2, 1, 3], True],
        [[1, 2, 2], [2, 1, 1], False],
        [[1, 1, 4], [1, 2, 3], False],
        [[1, 2, 3], [1, 10, 2], False],
        [[2, 3, 1], [1, 3, 2], True],
        [[2, 3, 9], [10, 3, 2], False],
        [[4, 6, 3], [3, 4, 6], False],
        [
            [832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
            [832, 998, 148, 570, 533, 561, 455, 147, 894, 279],
            True],
        [
            [832, 998, 148, 570, 533, 561, 894, 147, 455, 279],
            [832, 570, 148, 998, 533, 561, 455, 147, 894, 279],
            False
        ],
        [[1, 2, 3, 4, 4, 7, 5], [1, 2, 3, 5, 4, 7, 4], True]
    ]

    for t in tests:
        res = areSimilar(t[0], t[1])
        if t[2] == res:
            print("PASSED: areSimilar({}, {}) returned {}"
                  .format(t[0], t[1], res))
        else:
            print("FAILED: areSimilar({}, {}) returned {}, answer: {}"
                  .format(t[0], t[1], res, t[2]))


if __name__ == '__main__':
    main()
