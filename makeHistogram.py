# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:04:09 2021

@author: Jospin Amisi
"""

"""

You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):

Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification

Restrictions:

- Do not paste import pylab in the box.
- You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
- Do not leave any debugging print statements when you paste your code in the box.


"""

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()