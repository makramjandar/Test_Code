#!/usr/local/bin/python3


def main():
    # Test suite

    matrix_1 = [
        [1, 0],
        [1, 1]
    ]

    result_1 = [
        [0, 0],
        [1, 0]
    ]

    matrix_2 = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    result_2 = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    tests = [
        [None, None], # Should throw a TypeError
        [matrix_1, result_1],
        [matrix_2, result_2]
    ]

    for item in tests:
        try:
            print('Matrix: {}'.format(item[0]))
            temp_result = zero_row_col_matrix(item[0])
            if temp_result == item[1]:
                print('PASSED: zero_row_col_matrix() returned {}'.format(temp_result))
            else:
                print('FAILED: zero_row_col_matrix() returned {}, should have returned {}'.format(temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def zero_row_col_matrix(matrix):
    '''
    Finds the zeroes in a given matrix and zeroes out the entire row and column they are in. Done in place
    Input: MxN matrix
    Output: MxN matrix
    '''
    # Input checks
    if type(matrix) is not list:
        raise TypeError('Matrix must be a list')
    if type(matrix[0]) is not list:
        raise TypeError('Matrix must be a list of lists')

    M = len(matrix)
    N = len(matrix[0])
    row_flag = False

    # Check if first row has a zero
    if 0 in matrix[0]:
        row_flag = True
    # Check if first column has a zero, use matrix[0][0] to store info
    for r in range(M):
        if matrix[r][0] == 0:
            matrix[0][0] = 0
            break

    # Check rest of matrix from r/c 1 to end, save zero in first row and col
    for r in range(1, M):
        for c in range(1, N):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # Change inner part of matrix if row or column are zero
    for r in range(1, M):
        for c in range(1, N):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # Zero out the first row and column if necessary
    if matrix[0][0] == 0: # first column should be all zeroes
        for r in range(M):
            matrix[r][0] = 0

    if row_flag:
        for c in range(N):
            matrix[0][c] = 0

    return matrix


if __name__ == '__main__':
    main()
