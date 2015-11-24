import asyncio
import urllib.parse
import sys

@asyncio.coroutine
def print_http_header(url):
    url = urllib.parse.urlsplit(url)
    reader, writer = asyncio.open_connection(url.hostname, 80)
    query = ('HEAD {url.path} HTTP/1.0\r\n'
            'HOST: {url.hostname}\r\n'
            '\r\n').format(url=url)
    writer.write(query.encode('latin-1'))
    while True:
        line = yield from reader.readline()
        if not line:
            break
        line = line.decode('latin-1').rstrip()
        if line:
            print('HTTP header> %s' % line)

url = sys.argv[1]
loop = asyncio.get_event_loop()
task = asyncio.async(print_http_header(url))
loop.run_until_complete(task)
loop.close()
