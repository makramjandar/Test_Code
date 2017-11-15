#!/usr/local/bin/python
# edX Intro to Computational Thinking and Data Science
# Graphs - Depth First Search to find shortest path lecture code

import graphs


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph: start and end are nodes; path and shortest
        are lists of nodes.
    Returns a shortest path from start to end in graph"""

    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))

    if start == end:
        return path

    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)

    return shortest


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
    return DFS(graph, start, end, [], None, toPrint)


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
    test_shortest_path = False

    if test_shortest_path:
        testSP('Chicago', 'Boston')
        testSP('Boston', 'Phoenix')


if __name__ == '__main__':
    main()
