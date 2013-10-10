from twisted.internet import defer

from twisted.enterprise import adbapi


class DictStorage(object):

    def __init__(self):
        self._storage = {}

    def set(self, key, data):
        self._storage[key] = data
        return defer.succeed(None)

    def get(self, key):
        return defer.succeed(self._storage.get(key))

    def getAll(self):
        return defer.succeed(self._storage.copy())



class MySQLStorage(object):

    def __init__(self):
        self._pool = adbapi.ConnectionPool('MySQLdb', db='ersid')

    def set(self, key, data):
        d = self.get(key)

        def gotKey(result):
            if result:
                return self._pool.runOperation(
                    "UPDATE ersid_data SET ersid_value = %s WHERE "
                    "ersid_key = %s", (key, data))
            else:
                return self._pool.runOperation(
                    "INSERT INTO ersid_data VALUES (%s, %s)", (key, data))

        return d.addCallback(gotKey)

    def get(self, key):
        d = self._pool.runQuery(
            "SELECT ersid_value FROM ersid_data WHERE ersid_key = %s", (key,))

        def gotValue(value):
            if value:
                return value[0][0]

        return d.addCallback(gotValue)

    def getAll(self):
        return self._pool.runQuery(
            "SELECT ersid_key, ersid_value FROM ersid_data")
