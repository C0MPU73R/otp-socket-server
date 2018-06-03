from server.lib.Logger import Logger
from twisted.internet import protocol
from .ServerBase import ServerBase


class ServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        # to be overridden by inheritors
        pass
