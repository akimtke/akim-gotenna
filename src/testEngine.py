# -*- coding: utf-8 -*-

# This class handles the execution of the test.

#from tests import *

class testEngine(object):

    def __init__(self):
        pass

    # This method should be given a list of tests. Iterate through the tests
    # and execute. The results should be stored in the objects.
    def runTest(self, testSet, dev):
        for test in testSet:
            #test.execute(dev)
            print "Executing test"
