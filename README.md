# Ersid

Ersid is an educational example of a Twisted-based application.

It is a simple REST HTTP server that simply allows storage and retrieval of
arbitrary blobs.

When you run ./bin/service, the server will be started. It has three features:

- a REST HTTP server that listens on port 8080
- an interactive interpreter (using Twisted's manhole) accessible via SSH
  on port 8022.
- disk-based persistence; all data is saved to a dump file on an interval.


# Usage

After running ./bin/service, you can the following operations:

Set "mykey" to "myvalue":

    $ curl -XPOST -d myvalue http://localhost:8080/mykey

Fetch "mykey":

    $ curl http://localhost:8080/mykey


# Contributors

- Christopher Armstrong (http://github.com/radeex)
- Thomas Hervé (http://github.com/therve)
- Ying Li (http://github.com/cyli)
- Duncan McGreggor (http://github.com/oubiwann)


# License

Copyright (C) 2013 Rackspace, Inc.

Ersid is made available under the MIT license, as described below:

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
