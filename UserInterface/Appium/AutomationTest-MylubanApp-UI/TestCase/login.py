#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from PageObject.Login_pageObject import *

login = Login()
time.sleep(10)
try:
    login.swipeLeft(n=3)
    login.tap((270,760))

    login.inputUsername('xushenwei')
    login.inputPassword('111111')
    login.buttonLogin()
finally:
    login.quit()