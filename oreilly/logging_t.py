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
