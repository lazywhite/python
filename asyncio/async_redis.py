import asyncio
import asyncio_redis

@asyncio.coroutine
def my_subscriber(channel):
    #create connection
    connection = yield from asyncio_redis.Connection.create(host='localhost',
                                                            port=6379)
    subscriber = yield from connection.start_subscribe()
    yield from subscriber.subscribe(channel)
    while True:
        reply = yield from subscriber.next_published()
        print('Received: ', repr(reply.value), 'on', reply.channel)

loop = asyncio.get_event_loop()
asyncio.async(my_subscriber(['channel-1']))
#asyncio.async(my_subscriber('channel-2'))

loop.run_forever()
