# -*- coding: utf-8 -*-

# This class takes in a file and deserializes the data. Specialized decoding is
# implemented here.

from sys import argv
import sys
import json

from testConfig import testConfig
from device import Device
# Need to import all test and test factory classes. May need to restructure
# directories so this can be accomplished with a from dir import * clause.
from tests import *
from factories import *

class jsonReader(object):
    _instance = None

    # This class follows the Singleton design pattern. Only one instance of
    # this class can be created mostly to conserve space.
    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls._instance = super(jsonReader, cls).__new__(cls, *args, **kargs)
        return cls._instance

    # Initialization should be simple.
    def __init__(self):
        self.file = ""

    # Expects the file to be read to be passed in. The file is read and
    # deserialized. An array should be passed back that contains all the test
    # objects.
    def readFile(self, filename):
        with open(filename) as fileHandle:
            txt = fileHandle.read()

        # Call deserializer here
        #return json.loads(txt, object_hook=as_test)
        #return json.loads(txt)
        return json.loads(txt, object_hook=testConfig)

# Used to deserialize the JSON data into a test object. The type of test
# is determined by the value referenced by the "test" key. Not a part of any class
# so the JSON deserializer can access this function. This doesn't quite work but
# leaning towards trading this off and just reading the JSON as a dictionary for
# the configuration
def as_test(dct):
    if ('devices' in dct and 'testList' in dct):
        devArr = []
        while len(dct['devices']) > 0:
            x = dct['devices'].pop()
            devArr.append(Device(name = x['name'], port = x['port'], commType = x['commType'], commParams = x['commParams']))

        testArr = []
        while len(dct['testList']) > 0:
            data = dct['testList'].pop()
            func = '%sFactory' % data['name'].lower()
            factory = getattr(sys.modules[__name__], func)(data['type'], data['parameters'])
            testArr.append(factory.createTest())

        config = testConfig(devices = devArr, testList = testArr)
    else:
        config = testConfig()
    return dct
