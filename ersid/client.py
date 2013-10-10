from __future__ import print_function

import sys

import treq

from twisted.internet.task import react


class Client(object):

    def __init__(self, url):
        self.url = url

    def set(self, key, data):
        return treq.post("%s/%s" % (self.url, key), data)

    def get(self, key):
        return treq.get("%s/%s" % (self.url, key))


def display(response):
    return treq.text_content(response).addCallback(print)


def main(reactor, command=None, key=None, value=None):
    if not command and not key:
        sys.exit("Syntax: set/get key [value]")
    client = Client("http://localhost:8080")
    if command == "set":
        if not value:
            sys.exit("Syntax: set/get key [value]")
        return client.set(key, value)
    else:
        return client.get(key).addCallback(display)


if __name__ == "__main__":
    react(main, sys.argv[1:])
