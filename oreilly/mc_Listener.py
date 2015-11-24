# can't deal with more than one connection a time
from multiprocessing.connection import Listener 
import atexit 


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            msg = client.recv()
            if msg is None:
                break
            else:
                client.send(msg) 
        except :
            pass

def on_exit():
    import os
    os.remove(unix_domain_socket)

unix_domain_socket = '/tmp/test.sock'
ip_address = ('', 2500)
echo_server(unix_domain_socket, authkey=b'bob')

atexit.register(on_exit)

