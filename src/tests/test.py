class test(object):
    def __init__(self, name = "", logger):
        self.name = name
        self.logget = logger

    def execute(self, devConfig, testParams):
        raise NotImplementedError("Don't use the class test. Use a subclass.")

    def showTest(self):
        raise NotImplementedError("Don't use the class test. Use a subclass.")
