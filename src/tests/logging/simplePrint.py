from logInterface import logInterface
import time

class simplePrint(logInterface):
    """docstring for """
    def __init__(self, logLevel):
        super(, self).__init__()
        self.logLevel = logLevel

    # This version just prints to the screen.
    def log(self, msg, level):
        if(level <= self.logLevel):
            print "[%d] %d - %s" % (int(time.time()), level, msg)
