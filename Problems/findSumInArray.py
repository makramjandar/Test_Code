#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        [None, None, None], # Should throw a TypeError
        [[1, 2], 7.89, None], # Should throw a TypeError
        [[], 7, None], # Should throw a ValueError
        [[1, 3, 2, -7, 5], 7, [2, 4]]
    ]

    for item in tests:
        try:
            temp_result = two_sum(item[0], item[1])
            # if temp_result[0] == item[2][0] and temp_result[1] == item[2][1]:
            if temp_result == item[2]:
                print('PASSED: two_sum({}, {}) returned {}'.format(item[0], item[1], temp_result))
            else:
                print('FAILED: two_sum({}, {}) returned {}, should have returned {}'.format(item[0], item[1], temp_result, item[2]))

        except TypeError:
            print('PASSED TypeError test')

        except ValueError:
            print('PASSED ValueError test')

    return 0

def two_sum(nums, val):
    '''
    Given an array of ints, find indices of two numbers that sum to val
    Input: nums (array), val (int)
    Output: list with two indices of numbers in nums that sum to val
    Assumes nums is not sorted, returns an empty list if no answer
    '''
    if type(nums) is not list or type(val) is not int:
        raise TypeError('Input must be an array and an integer')

    if not nums:
        raise ValueError('First argument must be a non-empty array')

    complements = dict()

    for i, num in enumerate(nums):
        complement = val - num
        if num in complements.keys():
            # Found the complement in dict that matches with current number
            return [complements[num], i]
        else:
            # No match, save complement and index to dict
            complements[complement] = i
    return []


if __name__ == '__main__':
    main()
