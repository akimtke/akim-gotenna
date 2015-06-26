from tests import test

class testConfig(object):
    def __init__(self, devices = [], testList = []):
        self.devices = []
        self.testList = []

    def __getitem__(self, arg):
        print "%r" % arg
        return self

    def testSize(self):
        return len(self.testList)

    def printConfig(self):
        print "Devices"
        print "-----------"
        for dev in self.devices:
            dev.showDev()
        print "-----------"
        print "Tests"
        print "-----------"
        for test in self.testList:
            test.showTest()
        print "-----------"
