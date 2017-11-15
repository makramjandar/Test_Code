#!/usr/local/bin/python
# edX Intro to Computational Thinking and Data Science
# Graphs - Breadth First Search to find shortest path lecture code

import graphs


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path: {}'.format(printPath(pathQueue)))

    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path: {}'.format(printPath(tmpPath)))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)

    return None


def shortestPath(graph, start, end, toPrint=False):
    return BFS(graph, start, end, toPrint)


def testSP(source, destination):
    g = graphs.buildCityGraph(graphs.Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint=True)

    if sp is not None:
        print('Shortest path from {} to {} is {}'
              .format(source, destination, printPath(sp)))
    else:
        print('There is no path from {} to {}'.format(source, destination))


def main():
    testSP('Chicago', 'Boston')
    testSP('Boston', 'Phoenix')


if __name__ == '__main__':
    main()
