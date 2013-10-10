from twisted.internet import defer


class DictStorage(object):

    def __init__(self):
        self._storage = {}

    def set(self, key, data):
        self._storage[key] = data
        return defer.succeed(None)

    def get(self, key):
        return defer.succeed(self._storage.get(key))

    def getAll(self):
        return self._storage.copy()
