#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    spiral = spiral_order(matrix)
    print(spiral)


def spiral_order(matrix):
    '''
    Given an mxn matrix, returns the elements in spiral order
    Input: list of m lists, with n elements per list
    Output: list of elements in spiral order
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    returns: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    direction = 0 # 0: right, 1: down, 2: left, 3: up
    # Index for each edge of matrix
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    spiral = []

    while (left <= right and top <= bottom):
        if direction == 0:
            # Heading left to right
            for x in range(left, right+1):
                spiral.append(matrix[top][x])
            top += 1
        elif direction == 1:
            # Heading top to bottom
            for x in range(top, bottom+1):
                spiral.append(matrix[x][right])
            right -= 1
        elif direction == 2:
            # Heading right to left
            for x in range(right, left-1, -1):
                spiral.append(matrix[bottom][x])
            bottom -= 1
        elif direction == 3:
            # Heading bottom to top
            for x in range(bottom, top-1, -1):
                spiral.append(matrix[x][left])
            left += 1

        direction = (direction + 1) % 4

    return spiral


if __name__ == '__main__':
    main()
