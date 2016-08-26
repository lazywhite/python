import logging

# filter
# logger.addFilter()
# format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler = logging.FileHandler('./test.log',mode='a')
s_handler = logging.StreamHandler()

f_handler.setFormatter(formatter)
s_handler.setFormatter(formatter)
level = logging.DEBUG 
logger = logging.getLogger("main")
logger.setLevel(level)
logger.addHandler(f_handler)
logger.addHandler(s_handler)

logger.warning('warning')

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
