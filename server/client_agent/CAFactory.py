from server.lib.Logger import Logger
from server.core.ServerFactory import ServerFactory
from .ClientAgent import ClientAgent


class CAFactory(ServerFactory):
    logger = Logger("CAFactory")

    def buildProtocol(self, addr):
        return ClientAgent()
