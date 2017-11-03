#from io import StringIO

#s = StringIO()
#s.write('hello\n')
#print('test\n', file=s)
#print(s.getvalue())
#s.close()

#y = StringIO('haha\nfje\n')

#for i in y.readlines():
#    print(i,  end='')

#with open('a.txt', 'rb') as f:
#    data = f.read(20)
#    print(data)
#    print(data.decode('utf-8'))
# =========================

#import os.path
#def read_into_buffer(filename):
#    buf = bytearray(os.path.getsize(filename))
#    with open(filename, 'rb') as f:
#        f.readinto(buf)
#    return buf

#buf = read_into_buffer('a.txt')
#print(buf.decode('utf-8'))
#print(len(buf))
#print(buf[0:3])
# ==================
#import os
#import mmap

#def memory_map(filename, access=mmap.ACCESS_WRITE):
#    size = os.path.getsize(filename)
#    fd = os.open(filename, os.O_RDWR)
#    return mmap.mmap(fd, size, access=access)

#m =memory_map('a.txt')
#print(len(m))
#print(m[0:3])
# ====================
#import os.path
#path = '/usr/lib/python/a.csv'
#print(os.path.basename(path))
#print(os.path.dirname(path))
#print(os.path.join('tmp','data',os.path.basename(path)))
#path = '~/data.csv'
#print(os.path.expanduser(path))
#print(os.path.splitext(path))
#print(os.path.exists('/etc/passwd'))
#print(os.path.isfile('/etc/shadow'))
#print(os.path.islink('/usr/bin/python'))
#print(dir(os.path), end='\n\n')
#print(os.listdir())
# =======================
#import os.path
#import glob
#pyfiles = glob.glob('*.py')
#for i in pyfiles:
#    print(os.path.abspath(i))
# ====================
#import sys
#print(sys.getdefaultencoding())
#sys.stdout.write('fefe')
#sys.stdout.buffer.write(b'fefe')
# =====================

#from tempfile import TemporaryFile 

#with TemporaryFile('w+t') as f:
#    f.write('hello\n')
#    f.seek(2)
#    data = f.read()
#    print(data)

# =======================
# f.read(length)
# f.seek(position)
# f.tell() -> position
