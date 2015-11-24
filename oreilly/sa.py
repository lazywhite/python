#!/usr/bin/env python
#import fileinput

#with fileinput.input() as f:
#    for line in f:
#        print(line, end='')
# =========================
#raise SystemExit(1)
# ===========================
#import atexit
#def f(a,b,c):
#    print(a,b,c)

#atexit.register(f, *(1,2,3))
# ========================
## dest: argument store destination
## action:   store =>  into a string, overwrite  
#            append => into a list
#            store_true => boolean true
# metavar: used to generate help message
# nargs: accept n  arg
#import argparse

#parser = argparse.ArgumentParser(description='search some files')

#parser.add_argument(dest='filenames', metavar='filename', nargs='*')
#parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns',
#                    action='append', help='text pattern to search for')

#parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
#parser.add_argument('-o','--output', dest='outfile', action='store', help='output file')
#parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'},
#                    default='slow', help='search speed')
#args = parser.parse_args()

#print(args.filenames)
#print(args.patterns)
#print(args.verbose)
#print(type(args.outfile))
#print(args.speed)
# ===================================
#import getpass

#user = getpass.getuser() # get the username 
#user = input('enter your name')
#passwd = getpass.getpass() #won't display when you type in
#print(user,passwd)
# =====================================
#import os
#sz = os.get_terminal_size()
#print(sz.columns, sz.lines)
# ====================================
#import subprocess
#out = subprocess.check_output(['netstat','-ntlp'])
#out_text = out.decode('utf-8')
#print(out_text)
# =======================================
#import subprocess
#text = b'hello world'

#p = subprocess.Popen(['wc'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
#stdout, stderr = p.communicate(text)

#print(stdout, stderr)
# =====================================
#only for copying or moving files or directory , not deleting
#import shutil
#shutil.copy('sa.py','what.py')
#shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*pyc')
#shutil.copy('/root/.vimrc', '.vimrc')
# ==============================
#import shutil
#shutil.unpack_archive('/root/vim-7.4.tar.bz2', extract_dir='/tmp')
#shutil.make_archive('local','gztar','.')
# ===============================
#import os

#def find_file(start, name):
#    for relpath, dirs, files in os.walk(start):
#        if name in files:
#            full_path = os.path.join(start, relpath, name)
#            print(os.path.normpath(os.path.abspath(full_path)))
#find_file('/root','.vimrc')
# ===============================
from configparser import ConfigParser
#import pdb

cfg = ConfigParser()
#pdb.set_trace()
cfg.read('config.ini')
print(cfg.sections())
#print(cfg.get('installation', 'library'))
#print(cfg.getboolean('debug', 'log_errors'))
cfg.set('server','host','127.0.0.1')
cfg.set('server','port','2000')
#cfg.remove_option('server','port')
#print(cfg.get('server','port'))
with open('config.ini','wt') as f:
    cfg.write(f)
# ===============================
#import logging

#def main():
#    logging.basicConfig(
#            filename = '/var/log/app.log',
#            level = logging.ERROR,
#            format = '%(levelname)s:%(asctime)s:%(message)s'
#            )
#    logger = logging.getLogger()
#    hostname = 'www.python.org'
#    item = 'spam'
#    filename = 'data.csv'
#    mode = 'r'

#    logger.critical('host %s unknow', hostname)
#    logger.error('couldn\'t find %r', item)
#    logger.warning('feature is deprecated')
#    logger.info('opening file %r, mode=%r', filename, mode)
#    logger.debug('got here')

#if __name__ == '__main__':
#    main()
# ===============================
#import signal
#import resource
#import os

#def time_exceeded(signal, frame):
#    print('Time\'s up')
#    raise SystemExit(1)

#def set_max_runtime(seconds):
#    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
#    print(soft, hard)
#    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
#    signal.signal(signal.SIGXCPU, time_exceeded)

#def limit_memory(maxsize):
#    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
#    print(soft,hard)
#    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


#set_max_runtime(1)
#limit_memory(0)
#while True:
#    pass
