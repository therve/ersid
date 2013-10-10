from zope.interface import implements

from twisted.plugin import IPlugin
from twisted.application import service, internet

from twisted.web.server import Site
from twisted.python.usage import Options

from ersid import backdoor, rest, dump, storage


class ErsidOptions(Options):
    optParameters = [
        ['rest-port', 'p', 8080, 'Port of the ReST endpoint', int],
        ['manhole-port', 'm', 8022, 'Port of the Manhole endpoint', int],
        ['dump-interval', 'i', 10,
         'Time interval in seconds between each dump', int],
        ['dump-file', 'f',  '/tmp/dump', 'File used for dump'],
    ]


class ErsidPlugin(object):
    implements(IPlugin, service.IServiceMaker)

    tapname = "ersid"
    description = "Ersid service plugin"
    options = ErsidOptions

    def makeService(self, options):
        parent = service.MultiService()
        svc = rest.Service(storage.DictStorage())
        backdoorService = internet.TCPServer(
            options['manhole-port'], backdoor.makeFactory({'service': svc}))
        backdoorService.setServiceParent(parent)

        dumpService = internet.TimerService(
            options['dump-interval'], dump.backup, svc, options['dump-file'])
        dumpService.setServiceParent(parent)

        restService = internet.TCPServer(
            options['rest-port'], Site(svc.app.resource()))
        restService.setServiceParent(parent)
        return parent


ersidPlugin = ErsidPlugin()
