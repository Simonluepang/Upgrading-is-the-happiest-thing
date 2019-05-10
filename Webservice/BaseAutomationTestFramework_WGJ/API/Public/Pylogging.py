#coding=utf-8
import warnings,logging
warnings.filterwarnings("ignore")
from API.Setting import *
from logging import handlers

class Logger:
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }
    def __init__(self,filename,level='info',when='M',backCount=30,interval=1,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        if not self.logger.handlers:
            th = handlers.TimedRotatingFileHandler(filename=Path['Logging']+filename,when=when,interval=interval,backupCount=backCount,encoding='utf-8')
            th.suffix = "%Y%m%d_%H%M%S.log"
            th.setFormatter(format_str)
            self.logger.addHandler(sh)
            self.logger.addHandler(th)


if __name__ == '__main__':
    pass
