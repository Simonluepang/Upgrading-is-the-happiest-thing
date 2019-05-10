#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random, string, unittest, pytest, sys
from time import sleep
sys.path.append("./")
from page_obj.PageFunction import FunctionFactory
from myunit import CenterTest

class AddCompany(CenterTest):

    def add_company(self):
        FF = FunctionFactory(self.driver, 'add_company_css')
        message