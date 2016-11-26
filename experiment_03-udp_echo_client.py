import asyncio


class EchoClientProtocol:
    def __init__(self, message_, loop_):
        self.message = message_
        self.loop = loop_
        self.transport = None

    def connection_made(self, transport_):
        self.transport = transport_
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, address):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop_ = asyncio.get_event_loop()
        loop_.stop()

loop = asyncio.get_event_loop()
message = "Hello World!"
coro = lambda: EchoClientProtocol(message, loop)
print (type(coro))
if 0:
    connect = loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(message, loop),
        remote_addr=('127.0.0.1', 9999))
    print('endpoint created')
    transport, protocol = loop.run_until_complete(connect)
    print('endpoint completed')
    loop.run_forever()
    print('looped finished')
    transport.close()
loop.close()
