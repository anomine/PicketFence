import asyncio
from msvcrt import kbhit, getch
import time
from types import coroutine
## windows only console async input

loop = asyncio.get_event_loop()
from asyncio import Queue

myq = Queue()

@coroutine
def get_key_now():
    while True:
        #print('x')
        if not kbhit():
            pass
            yield from asyncio.sleep(0.1)
        else:
            ch = getch()
            print ('got now',ch)
            yield from myq.put(ch)

async def wait_q():
    while True:
        x = await myq.get()
        print('got q',x)


def print_key_now(ch):
    print('now',ch)

async def get_key(future):
    if 1:
        while True:
            if kbhit():
                ch = getch()
                print ('got ch',ch)
                future.set_result(ch)
                break
            await asyncio.sleep(0.1)
    #await asyncio.sleep(1)
    #future.set_result(b'x')

def print_key(future):
    ch = future.result()
    print('fut got key',ch)
    if ch==b'q':
        loop.stop()

async def monitor_keys():
    while True:
        if 0:
            coro_fut = asyncio.Future()
            coro_fut.add_done_callback(print_key)
            await get_key(coro_fut)
        else:
            coro = get_key_now()
            await asyncio.ensure_future(coro)
if 0:
    coro = monitor_keys()
    asyncio.gather(coro)
else:
    coro = get_key_now()
    coro_q = wait_q()
    asyncio.gather(coro,coro_q)

if 0:
    while True:
        print('waiting')
        if kbhit():
            print('got key',getch())
        time.sleep(0.2)
else:
    loop.run_forever()
    loop.close()