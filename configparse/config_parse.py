from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
cfg.set('server','host','127.0.0.1')
cfg.set('server','port','2000')

with open('config.ini','wt') as f:
    cfg.write(f)
