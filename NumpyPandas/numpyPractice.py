#!/Applications/anaconda/envs/dataAnalysisTut/bin

import numpy as np


def main():
    height = [1.73, 1.68, 1.71, 1.89, 1.79]
    weight = [65.4, 59.2, 63.6, 88.4, 68.7]

    np_height = np.array(height)
    np_weight = np.array(weight)

    print("Type of numpy array for heights: {}".format(type(np_height))) # numpy.ndarray

    np_2d = np.array([height, weight])

    print("2D array: {}".format(np_2d))
    print("Shape of 2D array: {}".format(np_2d.shape)) # Tuple (2, 5)

    # Subsetting - same as 2D lists or using [row, column]
    item1 = np_2d[0][2] # 1.71
    item2 = np_2d[0,2] # 1.71

    # Get height and weight for 2nd and 3rd person (both rows, cols 2&3)
    item3 = np_2d[:,1:3]

    # Just weight row
    weight_only = np_2d[1,:]
    print("Weight row is: {}".format(weight_only))

    # All info from 4th column
    fourthCol = np_2d[:,3]
    print("Fourth col is: {}".format(fourthCol))

    # Generate 5000 random normally distributed samples for heigh and weight
    # np.random.normal(mean, standard deviation, number of samples)
    city_height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
    city_weight = np.round(np.random.normal(6.32, 15, 5000), 2)
    np_city = np.column_stack((city_height, city_weight))
    print("Shape of city height and weight: {}".format(np_city.shape))

    # Stats - also uses .sum() and .sort()
    print("Average city height: {}".format(np.mean(np_city[:,0])))
    print("Average city weight: {}".format(np.mean(np_city[:,1])))
    print("Median city weight: {}".format(np.median(np_city[:,1])))
    print("Standard deviation of weight: {}".format(np.std(np_city[:,1])))
    correlated = np.corrcoef(np_city[:,0], np_city[:,1])
    print("Correlation coefficients: {}".format(correlated))






if __name__ == '__main__':
    main()
