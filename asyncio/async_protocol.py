import asyncio

class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        print('Connection made')
        self.transport = transport

    def data_received(self, data):
        print('Data received', data)
        if data.strip() == b'stop':
            global loop
            loop.call_soon(self.transport.pause_reading)
            loop.call_later(20,self.transport.resume_reading)
        self.transport.write(data)

    def connection_lost(self, exc):
        print('Connection lost')
        global server
        server.close()

loop = asyncio.get_event_loop()

server = loop.run_until_complete(loop.create_server(EchoProtocol,
                                'localhost', '4000'))
loop.run_until_complete(server.wait_closed())
