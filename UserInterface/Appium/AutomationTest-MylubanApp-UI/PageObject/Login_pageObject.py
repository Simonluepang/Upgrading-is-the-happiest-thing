#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Public.Base import *

class Login(Base):

    def inputUsername(self,username):
        self.location('ID','SENDKEYS','com.lubansoft.bimview4phone:id/account_edit_txt',message=username)

    def inputPassword(self,password):
        self.location('ID','SENDKEYS','com.lubansoft.bimview4phone:id/pwd_edit_txt',message=password)

    def buttonLogin(self):
        self.location('ID','CLICK','com.lubansoft.bimview4phone:id/login_btn')

    def buttonRegister(self):
        self.location('ID','CLICK','com.lubansoft.bimview4phone:id/tv_goto_register')

    def buttonForgetpwd(self):
        self.location('ID','CLICK','com.lubansoft.bimview4phone:id/tv_forget_pwd')

    def hintCopyright(self):
        return self.location('ID','HINT','com.lubansoft.bimview4phone:id/tv_app_copyright')