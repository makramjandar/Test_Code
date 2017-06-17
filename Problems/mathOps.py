#!/usr/local/bin/python3


def main():
    # Test suite
    sample = [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
    results = [9, 2, 5, (9, 2)] # max, min, mean, mode. Mode is 9 or 2

    solution = Solution()

    try:
        solution.insert(None)
    except TypeError:
        print('PASSED TypeError test')

    for v in sample:
        solution.insert(v)

    if solution.max == results[0]:
        print('PASSED: Max is {}'.format(solution.max))
    else:
        print('FAILED: Max is {}, should be {}'.format(solution.max, results[0]))

    if solution.min == results[1]:
        print('PASSED: Min is {}'.format(solution.min))
    else:
        print('FAILED: Min is {}, should be {}'.format(solution.min, results[1]))

    if solution.mean == results[2]:
        print('PASSED: Mean is {}'.format(solution.mean))
    else:
        print('FAILED: Mean is {}, should be {}'.format(solution.mean, results[2]))

    if solution.mode in results[3]:
        print('PASSED: mode is {}'.format(solution.mode))
    else:
        print('FAILED: mode is {}, should be {} or {}'.format(solution.mode, results[3][0], results[3][1]))


    return 0


class Solution(object):
    '''
    Class to insert an int into a list
    Also implements max, min, mean, and mode calculations in O(1)
    '''

    def __init__(self, upper_limit=100):
        self.upper_limit = upper_limit
        self._internal_list = []
        self._frequency_dict = {}
        self.max = None
        self.min = None
        self.mean = None
        self.freq = None
        self.mode = None
        self.sum = 0
        self.num_items = 0

    def insert(self, val):
        if type(val) is not int:
            raise TypeError

        # Update the max and min values
        if self.max is None or self.min is None:
            # First time setting maximum and minimum
            self.max = val
            self.min = val
        else:
            if val > self.max:
                self.max = val
            if val < self.min:
                self.min = val

        # Keep running total of sum to get mean
        self.sum += val
        self.num_items += 1
        self.mean = self.sum / self.num_items

        # Track the frequency of val in the list
        try:
            self._frequency_dict[val] += 1
        except KeyError:
            self._frequency_dict[val] = 1

        # Update mode (most frequently occurring value)
        if self.freq is None:
            # First time setting mode
            self.freq = (val, 1)
            self.mode = self.freq[0]
        else:
            temp_freq = self._frequency_dict[val]
            if temp_freq > self.freq[1]:
                self.freq = (val, temp_freq)
                self.mode = self.freq[0]

        self._internal_list.append(val)

        return self._internal_list


if __name__ == '__main__':
    main()
