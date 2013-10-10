import json

from twisted.internet.task import LoopingCall
from twisted.python import log


def backup(service, filename):
    d = service.storage.getAll()

    def gotAll(data):
        try:
            out = file(filename, 'w')
        except Exception, e:
            log.msg("Error opening %s for write: %s" % (filename, e))
            return
        dump_data = json.dumps(data)
        out.write(json.dumps(data))
        out.close()
        log.msg("Dumping %s keys in %s bytes to %s" % (
            len(data), len(dump_data), filename))

    return d.addCallback(gotAll)


def startLoop(interval, service, filename):
    loop = LoopingCall(backup, service, filename)
    loop.start(interval)
