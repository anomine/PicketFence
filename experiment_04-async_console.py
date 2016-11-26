import asyncio
from msvcrt import kbhit, getch
import time
from types import coroutine
## windows only console async input

loop = asyncio.get_event_loop()



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
        coro_fut = asyncio.Future()
        coro_fut.add_done_callback(print_key)
        await get_key(coro_fut)

coro = monitor_keys()
asyncio.gather(coro)

if 0:
    while True:
        print('waiting')
        if kbhit():
            print('got key',getch())
        time.sleep(0.2)
else:
    loop.run_forever()
    loop.close()