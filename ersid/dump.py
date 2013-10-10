import json

from twisted.internet.task import LoopingCall


def backup(service, filename):
    out = file(filename, 'w')
    out.write(json.dumps(service.storage.getAll()))
    out.close()


def startLoop(interval, service, filename):
    loop = LoopingCall(backup, service, filename)
    loop.start(interval)
