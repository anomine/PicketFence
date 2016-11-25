import asyncio


async def foo(data):
    """"sleep and return an increment"""
    print('foo', data)
    await asyncio.sleep(0.1)
    print('done foo')
    return data + 1

async def bar():
    """"sleep and return nothing"""
    print('bar')
    await asyncio.sleep(0.2)
    return 'done bar'

async def quit_it(loop):
    """"sleep and stop the loop"""
    print('quit handler')
    await asyncio.sleep(2)
    print('quit fired')
    loop.stop()
    return None

# get the event loop (aka reactor)
loop = asyncio.get_event_loop()

# instantiate the coroutines
foo_coro = foo(10)
bar_coro = bar()
quit_coro = quit_it(loop)

#schedule them (they don't run yet)

#use gather to create a single future from a list of coro's
tasks = asyncio.gather(*[foo_coro,bar_coro,quit_coro])

loop.run_until_complete(tasks)

if 0:
    # run the event loop, try and play nice and ensure that you clean up at the end, even on Keyboard Interrupt
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()
        print('loop closed')





