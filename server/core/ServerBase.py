from server.lib.Logger import Logger
from twisted.internet import endpoints, protocol, reactor


class ServerBase(protocol.Protocol):
    logger = Logger("ServerBase")

    def __init__(self):
        pass        

    def dataReceived(self, data):
        # to be overridden by inheritors
        pass
