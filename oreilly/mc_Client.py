from multiprocessing.connection import Client 
c = Client('/tmp/test.sock', authkey=b'bob')
c.send('adkfj')
print(c.recv())
