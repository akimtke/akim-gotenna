#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is the main script that should be run from command line.

from testEngine import testEngine
from jsonReader import jsonReader

from sys import argv
import os.path

# This function shows the usage of this tool.
def showUsage():
    print "python runTests.py [test_config]"

# This function displays data in a table manner that tries to figure out spacing.
# Currently working although the spacing thing doesn't work very well...
def fancyTable(arrays):

    def areAllEqual(lst):
        return not lst or [lst[0]] * len(lst) == lst

    if not areAllEqual(map(len, arrays)):
        exit('Cannot print a table with unequal array lengths.')

    verticalMaxLengths = [max(value) for value in map(lambda * x:x, *[map(len, a) for a in arrays])]

    spacedLines = []

    for array in arrays:
        spacedLine = ''
        for i, field in enumerate(array):
            diff = verticalMaxLengths[i] - len(field)
            spacedLine += field + ' ' * diff + '\t'
        spacedLines.append(spacedLine)

    return '\n'.join(spacedLines)

# Outputs results of a test into a table. Will need to make a secondary version
# of this method that outputs to a file.
def outputResults(tests):
    if len(tests) > 0:
        table = [["Test", "Result", "Message"]]
        for test in tests:
            row = [test.__class__.__name__, str(test.result), test.message]
            table.append(row)
        print fancyTable(table)

# Create an engine and a reader instance.
engine = testEngine()
decoder = jsonReader()
try:
    script, filename = argv
except ValueError:
    showUsage()
    exit()
filename = filename.strip()
if os.path.isfile(filename):
    tests = None
    while tests is None:
        tests = decoder.readFile(filename)
    # Used for debugging
    print "%r" % tests.printConfig()
    # Uncomment the following to use the test engine
    #engine.runTest(tests, ipindex)
    #outputResults(tests)
else:
    print "Cannot find file named %s" % filename
