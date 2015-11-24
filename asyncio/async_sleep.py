import asyncio 
import time

@asyncio.coroutine
def sleepy():
    time_before = time.time()
    print('before sleep', time_before)
    yield from asyncio.sleep(3)
    time_after = time.time()
    print('after sleep', time_after)
    print('time consumed',time_after - time_before) 

loop = asyncio.get_event_loop()
loop.run_until_complete(sleepy())
