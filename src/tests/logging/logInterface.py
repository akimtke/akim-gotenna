class logInterface(object):
    """docstring for """
    def __init__(self, level):
        super(, self).__init__()
        self.level = level

    def log(self, msg):
        raise NotImplementedError("Use subclass like simplePrint")
