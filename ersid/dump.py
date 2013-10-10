import json

from twisted.internet.task import LoopingCall


def backup(service, filename):
    d = service.storage.getAll()

    def gotAll(data):
        out = file(filename, 'w')
        out.write(json.dumps(data))
        out.close()

    return d.addCallback(gotAll)


def startLoop(interval, service, filename):
    loop = LoopingCall(backup, service, filename)
    loop.start(interval)
