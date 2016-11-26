import asyncio
"""Experiments with Futures"""

async def foo(future,data):
    """"sleep and return an increment"""
    print('foo',data)
    await asyncio.sleep(0.1)
    print('done foo')
    future.set_result(data + 1)


async def bar(future):
    """"sleep and return nothing"""
    print('bar')
    await asyncio.sleep(0.2)
    future.set_result('done bar')


async def quit_it(loop_):
    """"sleep and stop the loop"""
    print('quit handler')
    await asyncio.sleep(2)
    print('quit fired')
    loop_.stop()
    return None


def print_foo_result(future):
    print('foo result {}'.format(future.result()))


def print_bar_result(future):
    print('bar result {}'.format(future.result()))


# get the event loop (aka reactor)
loop = asyncio.get_event_loop()

foo_future = asyncio.Future()
bar_future = asyncio.Future()

# instantiate the coroutines
foo_coro = foo(foo_future,10)
bar_coro = bar(bar_future)
quit_coro = quit_it(loop)

#add callbacks from the future
foo_future.add_done_callback(print_foo_result)
bar_future.add_done_callback(print_bar_result)

# schedule them (they don't run yet)

# use gather to create a single future from a list of coro's
tasks = asyncio.gather(*[foo_coro, bar_coro, quit_coro])
print('waiting on tasks for {}'.format(__file__))
if 1:
    # run the event loop, try and play nice and ensure that you clean up at the end, even on Keyboard Interrupt
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()
        print('loop closed')
