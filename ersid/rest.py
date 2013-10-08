from klein import Klein


class Service(object):
    app = Klein()

    def __init__(self):
        self.storage = {}

    @app.route('/<key>', methods=['POST'])
    def set_key(self, request, key):
        self.storage[key] = request.content.getvalue()


    @app.route('/<key>', methods=['GET'])
    def get_key(self, request, key):
        return self._storage[key]


__all__ = ['Service']
