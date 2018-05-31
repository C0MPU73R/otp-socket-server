from server.core.ServerBase import ServerBase
from server.lib.MessageTypes import MessageTypes as msg_types
from server.lib.Logger import Logger

from ByteArray import ByteArray


class ClientAgent(ServerBase):
    logger = Logger("ClientAgent")

    def __init__(self, host, port):
        ServerBase.__init__(self, host, port)

    def configure(self):
        ServerBase.setup_socket(self)

    def handle_data(self, data):
        dg = ByteArray(data)
        
        msg = dg.readUnsignedInt()

        if msg == msg_types.HEARTBEAT.value:
            self.handle_heartbeat()
        elif msg == msg_types.CLIENT_DISCONNECT.value:
            self.handle_disconnect()
        else:
            self.logger.debug("unknown message received - {}".format(msg))

    def handle_heartbeat(self):
        # TODO - keep track of client heartbeats
        self.logger.debug("got client heartbeat")

    def handle_disconnect(self):
        # TODO - remove connection from connection list
        self.logger.warn("client disconnected")
