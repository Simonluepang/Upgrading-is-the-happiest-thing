#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.AuthController import *

if __name__ == '__main__':
    print(SaveUserProjectInfo().save_user_project_info(SaveUserProjectInfo().req_params()))