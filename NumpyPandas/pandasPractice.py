#!/Applications/anaconda/envs/dataAnalysisTut/bin

import pandas as pd


def main():
    # Create DataFrame from csv file information
    family = pd.read_csv("familyInfo.csv", index_col=0)
    print("Full Data Set:\n{}".format(family))

    # Access columns - new series or DataFrame
    heightSeries = family["Height"]
    heightDF = family[["Height"]]

    # Access subsets (one row, some rows, some columns)
    # One row
    #me = family.loc["Me"] # new series
    me = family.loc[["Me"]] # new DataFrame
    # print("\nMe:\n{}".format(me))

    # Some rows, all columns
    siblings = family.loc[["Sis", "Bro", "Me"]]
    print("\nSibling rows:\n{}".format(siblings))

    # Some rows, one column
    parentsWeight = family.loc[["Mom", "Dad"], ["Weight"]]
    print("\nParent rows, just weight:\n{}".format(parentsWeight))

    # Add a new column for BMI (weight (kg) / height (m)^2)
    family["BMI"] = round(family["Weight"] / family["Height"]**2, 2)
    print("Add BMI column:\n{}".format(family))



if __name__ == '__main__':
    main()
