#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by hubiao on 2017/5/17
from __future__ import  unicode_literals
from functools import wraps
from Common.Log import Log

log = Log()
log.set_logger()
def CaseAssertion(attempt=3):
    '''
    用例装饰器
    :param attempt: 重试次数
    :return: 
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            att = 0
            while att < attempt:
                try:
                    log.i('--> %s', func.__name__)
                    ret = func(*args, **kwargs)
                    log.i('<-- %s, %s\n',func.__name__,'Success')
                    return ret
                except AssertionError as e:
                    log.e('AssertionError, %s', e)
                    log.e('<-- %s, %s, %s\n',func.__name__,'AssertionError','Fail')
                    raise AssertionError(e)
                except Exception as e:
                    log.e('Exception, %s', e)
                    log.e('<-- %s, %s, %s\n',func.__name__,'Exception','Error')
                    if att ==2:
                        raise Exception(e)
                    att += 1
        return wrapper
    return decorator

def retry(attempt):
    '''
    重试装饰器
    :param attempt: 重试次数
    :return: 返回函数本身
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            att = 0
            while att < attempt:
                try:
                    return func(*args, **kw)
                except Exception as e:
                    att += 1
        return wrapper
    return decorator