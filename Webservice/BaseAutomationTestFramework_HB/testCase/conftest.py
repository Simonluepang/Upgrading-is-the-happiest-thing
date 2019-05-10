#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2018/10/9 18:07
# @Author  : hubiao
# @File    : conftest.py
import pytest
from util import HttpMethod
from util import PublicLogin
from util.Config import ManageConfig

pytest_plugins = 'pytester'

cf = ManageConfig()
pds = cf.getConfig('pds')

@pytest.fixture(scope="session")
def BimAadminLogin():
    '''
    BIM Aadmin运维管理系统登录
    :return:
    '''
    sysadmin = cf.getConfig('sysadmin')
    BimAadminLogin = HttpMethod.sendRequest(sysadmin['host'], sysadmin['header'])
    yield BimAadminLogin

@pytest.fixture(scope="session")
def CenterCAS():
    '''
    获取Center CAS登录凭证
    :return:
    '''
    PublicLogin.Center(pds["centerusername"], pds["centerpassword"]).Login()
    yield

@pytest.fixture(scope="session")
def CenterBuilder(CenterCAS):
    '''
    获取Builder登录凭证
    :return:
    '''
    CenterBuilder = HttpMethod.sendRequest(pds['builder'], pds['header'])
    yield CenterBuilder

@pytest.fixture(scope="session")
def PDSCAS():
    '''
    获取PDS登录凭证
    :return:
    '''
    username = cf.getConfig("sysadmin")['newusername']
    password = "96e79218965eb72c92a549dd5a330112"
    PublicLogin.BV(username, password).Login()
    yield

@pytest.fixture(scope="session")
def LBBV(PDSCAS):
    '''
    获取LBBV登录凭证
    :return:
    '''
    LBBV = HttpMethod.sendRequest(pds['lbbv'], pds['header'])
    yield LBBV

@pytest.fixture(scope="session")
def BimCO(PDSCAS):
    '''
    获取BimCO登录凭证
    :return:
    '''
    BimCO = HttpMethod.sendRequest(pds['bimco'], pds['header'])
    yield BimCO
