from klein import Klein


class Service(object):
    app = Klein()

    def __init__(self, storage):
        self.storage = storage

    @app.route('/<key>', methods=['POST'])
    def set_key(self, request, key):
        return self.storage.set(key, request.content.getvalue())


    @app.route('/<key>', methods=['GET'])
    def get_key(self, request, key):
        d = self.storage.get(key)

        def gotKey(data):
            if data is None:
                request.setResponseCode(404)
                return 'Not found'
            return data

        return d.addCallback(gotKey)


__all__ = ['Service']
