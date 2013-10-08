from klein import route, resource


_storage = {}


@route('/<key>', methods=['POST'])
def set_key(request, key):
    _storage[key] = request.content.getvalue()


@route('/<key>', methods=['GET'])
def get_key(request, key):
    return _storage[key]


__all__ = ['resource']
