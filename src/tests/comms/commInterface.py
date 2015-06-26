class commInterface(object):
    def __init__(self):
        pass

    def put(self, msg):
        raise NotImplementedError("Use subclass")

    def get(self):
        raise NotImplementedError("Use subclass")
