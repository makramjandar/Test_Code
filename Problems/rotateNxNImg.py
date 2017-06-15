#!/usr/local/bin/python3


def main():
    # Test suite

    image_1 = [
        [1, 2],
        [3, 4]
    ]

    result_1 = [
        [3, 1],
        [4, 2]
    ]

    image_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    result_2 = [
        [13,9,5,1],
        [14,10,6,2],
        [15,11,7,3],
        [16,12,8,4]
    ]

    tests = [
        [None, None], # Should throw a TypeError
        [[[1,2,3],[4,5,6]], None], # Should throw a ValueError
        [image_1, result_1],
        [image_2, result_2]
    ]

    for item in tests:
        try:
            print('Matrix: {}'.format(item[0]))
            temp_result = rotate_nbyn_img(item[0])
            if temp_result == item[1]:
                print('PASSED: rotate_nbyn_img() returned {}'.format(temp_result))
            else:
                print('FAILED: rotate_nbyn_img() returned {}, should have returned {}'.format(temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

        except ValueError:
            print('PASSED ValueError test')

    return 0


def rotate_nbyn_img(image):
    '''
    Rotates the pixels of an image by 90 degrees to the right, in place
    Input: image represented by an NxN matrix
    Output: NxN matrix
    '''
    # Input checks
    if type(image) is not list:
        raise TypeError('Image must be a list')
    if type(image[0]) is not list:
        raise TypeError('Image must be a list of lists')

    N = len(image)
    if N != len(image[0]):
        raise ValueError('Image must be an NxN matrix')

    layers = (N + 1) // 2 # rotate the pixels by layer, outermost first
    for layer in range(layers):
        last = N - 1 - layer
        for i in range(layer, last):
            offset = i - layer
            # Save top
            temp = image[layer][i]

            # Move left to top
            image[layer][i] = image[last-offset][layer]

            # Move bottom to left
            image[last-offset][layer] = image[last][last-offset]

            # Move right to bottom
            image[last][last-offset] = image[i][last]

            # Move top (temp) to right
            image[i][last] = temp


    return image



if __name__ == '__main__':
    main()
