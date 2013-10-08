from twisted.conch.insults import insults

from twisted.conch.manhole import ColoredManhole
from twisted.conch.manhole_ssh import ConchFactory, TerminalRealm

from twisted.cred import checkers, portal


def makeFactory(namespace):
    checker = checkers.InMemoryUsernamePasswordDatabaseDontUse(
        username='password')

    def chainProtocolFactory():
        return insults.ServerProtocol(ColoredManhole, namespace)

    rlm = TerminalRealm()
    rlm.chainedProtocolFactory = chainProtocolFactory
    ptl = portal.Portal(rlm, [checker])
    return ConchFactory(ptl)


__all__ = ['makeFactory']
