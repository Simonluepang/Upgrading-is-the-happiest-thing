#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""角色Controller"""

class FindRoles(CenterInterface):
    def find_roles(self):
        url = self.builder + '/roleRest/findRoles'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp