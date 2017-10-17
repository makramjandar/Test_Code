#!/usr/local/bin/python
# 0/1 Knapsack Problem - Greedy Algorithm Implementation


class Food(object):
    """Create a food object with name, value, and calories"""

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' +\
            str(self.calories) + '>'


def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
        name a list of strings
        values and calories lists of numbers
        returns list of Foods"""

    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    """Assumes items is a list, maxCost >= 0
        keyFunction maps elements of items to numbers, defines sorting order
        Assumes items have getCost and getValue methods that return numbers
        """
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)


def main():
    pass


if __name__ == '__main__':
    main()
