from twisted.web.server import Site
from twisted.application import service, internet

from ersid import backdoor, rest, dump, storage

svc = rest.Service(storage.DictStorage())

application = service.Application("Ersid application")

backdoorService = internet.TCPServer(8022, backdoor.makeFactory({'service': svc}))
backdoorService.setServiceParent(application)

dumpService = internet.TimerService(10, dump.backup, svc, '/tmp/dump')
dumpService.setServiceParent(application)

restService = internet.TCPServer(8080, Site(svc.app.resource()))
restService.setServiceParent(application)
