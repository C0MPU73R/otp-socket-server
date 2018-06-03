from server.lib.Logger import Logger
from server.core.ServerBase import ServerBase


class ClientAgent(ServerBase):
    logger = Logger("ClientAgent")

    def connectionMade(self):
        self.logger.warn("new connection to CA")

    def connectionLost(self, reason):
        self.logger.warn("lost connection from CA")

    def dataReceived(self, data):
        self.logger.debug("data received - {}".format(data))
