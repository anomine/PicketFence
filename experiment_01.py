import asyncio

async def f(foo):
    print('foo', foo)
    await asyncio.sleep(0.1)
    print('done foo')
    return foo+1

async def bar():
    print('bar')
    await asyncio.sleep(0.2)
    return 'done bar'

async def quitit(loop):
    print('quit handler')
    await asyncio.sleep(2)
    loop.stop()
    return None

loop = asyncio.get_event_loop()

foro = f(10)
boro = bar()
quitter = quitit(loop)

futs = [asyncio.ensure_future(x) for x in [foro,boro,quitter]]

if 1:
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()
        print('loop closed')





