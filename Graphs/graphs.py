#!/usr/local/bin/python
# edX Intro to Computational Thinking and Data Science
# Graphs lecture code


class Node(object):
    """docstring for Node"""

    def __init__(self, name):
        """ Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    """docstring for Edge"""

    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
