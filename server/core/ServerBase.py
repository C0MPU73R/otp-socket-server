from server.lib.Logger import Logger
import socket


class ServerBase:
    logger = Logger("ServerBase")

    def __init__(self, host, port, backlog=10000):
        self.host = host
        self.port = port
        self.backlog = backlog

    def setup_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        self.logger.info("socket binding on port {}".format(self.port))
        sock.listen(self.backlog)

        while True:
            (clientsock, addr) = sock.accept()
            try:
                self.logger.warn("new connection from {}".format(addr))
                while True:
                    data = clientsock.recv(1024)
                    if data:
                        self.handle_data(data)
                    else:
                        break
            finally:
                clientsock.close()

    def handle_data(self, data):
        # to be overridden by inheritors
        pass
