from twisted.internet import endpoints, reactor
from server.client_agent.CAFactory import CAFactory

ca = endpoints.TCP4ServerEndpoint(reactor, 6667)
ca.listen(CAFactory())
reactor.run()
