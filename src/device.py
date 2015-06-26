class Device(object):
    def __init__(self, name = "", port = "", commType = "", commParams = None):
        self.name = name
        self.port = port
        self.commType = commType
        self.commParams = commParams

    def showDev(self):
        print "Name: %r" % self.name
        print "\tPort: %r " % self.port
        print "\tComm Type: %r" % self.commType
        print "\tComm Params: %r" % self.commParams
