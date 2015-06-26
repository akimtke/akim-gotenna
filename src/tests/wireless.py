#!/usr/bin/env python

from test import test
from sys import argv
import json
import os.path
from comms import serialInterface
from time import sleep
from logging import simplePrint

# This class is for the stress test which sends a bunch of packets between
# devices. The class inherits and implements functions defined in the test
# class. The most important being execute as that is how the test engine
# runs the test without a care for what kind of test it is
class wirelessStress(test):

    # Name is pretty evident. This should be used to preface the logger line.
    # The logger should be a class implementing logInterface so the function
    # calls are the same. That way, the logger can be replaced by a different
    # kind even though the support structure for that isn't set up yet
    def __init__(self, name = "", logger):
        self.name = name
        self.logger = logger

    # This was put into a separate function in order to try and clean things up.
    # It was also added because of numerous aspects I thought may come into
    # play later on. For example, working with more than 2 radios and figuring
    # out which ones to test. Or if one device can output on more channels than
    # the other
    def TRXPackets(self, TXDev, RXDev, numChannels, numPackets):
        for chan in range(0, numChannels - 1):
            for n in range(0, numPackets):
                msg = "message # %d" % (n)
                Exec_cli_cmd(RXDev["port"], "Chan %d start_receive true" % chan)
                Exec_cli_cmd(TXDev["port"], "Chan %d Send_msg %s" % (chan, msg))
                sleep((len(msg) / 1250) * 1.25) # assumes 10kbps tx rate with 25% fudge room
                Exec_cli_cmd(RXDev["port"], "Chan %d start_receive false" % chan)
                response = get_text_log(TXDev["port"])
                self.logger.log("[%s] %s Chan %d log: %s" % (self.name, TXDev["name"], chan, response), 3)
                if response.find(msg) < 0:
                    self.logger.log("[%s] %s : Message corrupted before sending" % (self.name, TXDev["name"]), 0)
                else:
                    response = get_text_log(RXDev["port"])
                    self.logger.log("[%s] %s Chan %d log: %s" % (self.name, RXDev["name"], chan, response), 3)
                    if response.find("Received") < 0:
                        self.logger.log("[%s] %s : Message not received" % (self.name, RXDev["name"]), 0)
                    elif response.find(msg) < 0:
                        self.logger.log("[%s] %s : Message was corrupted" % (self.name, RXDev["name"]), 0)
                    else:
                        self.logger.log("[%s] %s : Message received" % (self.name, RXDev["name"]), 3)

    def execute(self, devConfig, testParams):
        print "Running"
        iterations = testParams[0]
        # Done this way because testing to make sure there are the same number of channels
        # can get a bit tedious. Might be necessary if dealing with different
        # radios are with legacy devices
        channels = testParams[1]
        # This assumes only 2 devices but can be expanded for more
        TRXPackets(devConfig[0], devConfig[1], channels, iterations)
        TRXPackets(devConfig[1], devConfig[0], channels, iterations)

    def showTest(self):
        print "Name: %r" % self.name

# Add some more test classes here:
# - wirelessLength - Test message length
# - wirelessSpecialChars - Test special characters getting sent through
# - wirelessCases - Test what happens when the devices sends data in RX mode

if __name__ == "__main__":
    # If this module is run as main, then execute just this test.
    # Running just this should be used as a test to do a quick check of the
    # test.

    # Read the arguments and make sure they follow the usage. If not, print
    # the usage
    try:
        script, filename = argv
    except ValueError as e:
        print "python wireless.py [Config File]"
        exit()

    # Make sure the file exists and then read the file
    filename = filename.strip()
    if os.path.isfile(filename):
        with open(filename) as file_handle:
            txt = file_handle.read()

        # Parse the json configuration file
        config = json.loads(txt)

        # Make sure the configuration file has the needed data
        if 'testList' in config:
            if 'devices' in config:
                # Need to find all wireless tests and execute them
                for test in config["testList"]:
                    if test["name"] == "wireless":
                        if test["type"] == "stress":
                            stressTest = wirelessStress(name = "StressTest", simplePrint(3))
                            stressTest.execute(config["devices"], test["parameters"])
            else:
                print "JSON file is not configured correctly (Devices)"
        else:
            print "JSON file is not configured correctly (Test List)"
    else:
        print "Cannot find file"
