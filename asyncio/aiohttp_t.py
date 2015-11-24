import aiohttp
import asyncio

@asyncio.coroutine
def fetch(url):
    resp = yield from aiohttp.request('GET', url)
    body = yield from resp.read()
    print(body.decode('utf-8'))


url = 'http://openapi.baidu.com/public/2.0/translate/dict/simple?client_id=hvTzXrjHIFETZ3nR534oDYTf&q=do&from=en&to=zh'

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch(url))
