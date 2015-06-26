from commInterface import commInterface

class serialInterface(commInterface):
    def __init__(self, port):
        self.port = port

    def put(self, channel, msg):
        Exec_cli_cmd(self.port, "%s start_recieve true" % channel)
        Exec_cli_cmd(self.port, "%s Send_msg %s" % (channel, msg))

    def get(self, channel, timeout):
        Exec_cli_cmd
