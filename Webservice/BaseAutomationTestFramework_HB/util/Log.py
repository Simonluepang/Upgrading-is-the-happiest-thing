#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by hubiao on 2017/5/12
from __future__ import  unicode_literals
import logging,os,time
from logging.handlers import TimedRotatingFileHandler
import re


class Log(object):

    def __init__(self):
        self.ResultRoot= './TestResult'

        if not os.path.exists(self.ResultRoot):
            os.mkdir(self.ResultRoot)

        date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.ResultFile = self.ResultRoot + '/' + date_time
        if not os.path.exists(self.ResultFile):
            os.mkdir(self.ResultFile)



    def set_logger(self):
        self.logger = logging.getLogger('Bussiness')
        self.logger.setLevel(logging.INFO)
        filename = self.ResultFile + '/' + 'Bussiness_' + time.strftime('%H%M%S', time.localtime(time.time())) + '.log'

        fh = logging.FileHandler(filename)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s]:%(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def initLogging(self,logFileName='applog'):
        '''
        初始化日志，日志按天分割，保存最近7天的日志记录
        :param logFileName: 日志文件名称，默认为applog
        :return: 无返回
        '''
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        log = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s]:%(message)s')
        LogFileHander = TimedRotatingFileHandler(filename=PATH('../log/' + logFileName), when='D', interval=1,
                                                 backupCount=7)
        LogFileHander.suffix = "%Y-%m-%d.log"
        LogFileHander.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        LogFileHander.setFormatter(formatter)
        log.setLevel(logging.DEBUG)
        log.addHandler(LogFileHander)



    def d(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
