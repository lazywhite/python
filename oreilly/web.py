#from urllib import request, parse

#url = 'http://localhost:8000'

#params = {
#        'name1':'value1',
#        'name2':'value2'
#        }

#query_string = parse.urlencode(params)
#print(query_string)
#u = request.urlopen(url+'?'+ query_string)
#u = request.urlopen(url, query_string.encode('ascii'))
#u = request.urlopen(url)

#resp = u.read().decode('utf-8')
#print(resp)
# ===========================
#import requests

#url = 'http://localhost:8000'

#params = {
#        'name1':'value1',
#        'name2':'value2'
#        }

#headers = {
#        'User-agent': 'none/ofyourbusniss',
#        'Spam' : 'Eggs'
#        }
#resp = requests.get(url, headers=headers )
#print(resp.text)

# ================================
#import requests

#url = 'http://localhost:8000'
#resp = requests.head(url)

#status = resp.status_code
#content_type = resp.headers['content-type']
#content_length = resp.headers['content-length']

#print(content_type, content_length)

# ==============================
#from http.client import HTTPConnection

#c = HTTPConnection('127.0.0.1',8000)
#c.request('HEAD', '/')
#resp = c.getresponse()

#print('status:',resp.status)
#for name, value in resp.getheaders():
#    print(name, value)
# ==========================

# this server can only handle one client a time
#from socketserver import BaseRequestHandler, TCPServer

#class EchoHandler(BaseRequestHandler):
#    def handle(self):
#        print('Got connection from', self.client_address)
#        while True:
#            msg = self.request.recv(8192)
#            if not msg:
#                break
#            self.request.send(msg)

#server = TCPServer(('',2000), EchoHandler)
#server.serve_forever()
# =============================
# Forking and Threading , but no upper limit
#from socketserver import BaseRequestHandler, ForkingTCPServer

#class EchoHandler(BaseRequestHandler):
#    def handle(self):
#        print('Got connection from', self.client_address)
#        while True:
#            msg = self.request.recv(8192)
#            if not msg:
#                break
#            self.request.send(msg)

#server = ForkingTCPServer(('',2000), EchoHandler)
#server.serve_forever()
# ==============================

#from threading import Thread

#from socketserver import BaseRequestHandler, TCPServer

#class EchoHandler(BaseRequestHandler):
#    def handle(self):
#        print('Got connection from', self.client_address)
#        while True:
#            msg = self.request.recv(8192)
#            if not msg:
#                break
#            self.request.send(msg)
# there will be n+1 threading 
#worker_limit = 1
#server = TCPServer(('',2000), EchoHandler)

#for i in range(worker_limit):
#    t = Thread(target=server.serve_forever)
#    t.daemon = True
#    t.start()

#server.serve_forever()
# =================================
#import ipaddress

#net = ipaddress.ip_network('192.168.1.0/22')
#net = ipaddress.ip_network('192.168.8.0/22')

#print(net.broadcast_address)
#print(net.netmask)
#print(net.num_addresses)
#a = ipaddress.ip_address('192.168.10.1')
#print(a in net)
# ==================================
