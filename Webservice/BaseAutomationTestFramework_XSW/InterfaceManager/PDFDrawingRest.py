#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from InterfaceManager.CenterInterfaceModel import *
"""PDS图纸相关"""

class GetDrawingDetailInfos(CenterInterface):
    # 获取图纸详情
    def req_params(self):
        params = {
              "classifyId": 0,
              "pageParam": {
                "orders": [
                  {
                    "direction": 0,
                    "property": "string"
                  }
                ],
                "page": 0,
                "size": 0
              },
              "ppid": 0,
              "searchKey": "string"
            }
        return params

    def certain_params(self):
        params = {
              "classifyId": -1,
              "pageParam": {
                "orders": [],
                "page": 1,
                "size": 0
              },
              "ppid": -1,
              "searchKey": ""
            }
        return params

    def get_drawing_detail_infos(self,data):
        url = self.builder + '/rs/pdfDrawingRest/getDrawingDetailInfos'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetDrawingClassifyInfos(CenterInterface):
    # 获取图纸的分类下拉框列表简要信息
    def get_drawing_classify_infos(self):
        url = self.builder + '/rs/pdfDrawingRest/getDrawingClassifyInfos'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class UpdateDrawingInfo(CenterInterface):
    # 修改图纸工程
    def req_params(self,classifyId,drawingId,drawingName,memo,ppid):
        params = {
              "classifyId": classifyId,
              "drawingId": drawingId,
              "drawingName": drawingName,
              "memo": memo,
              "ppid": ppid
            }
        return params

    def update_drawing_info(self,data):
        url = self.builder + '/rs/pdfDrawingRest/updateDrawingInfo'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp

class GetProjHasPdfDraw(CenterInterface):
    # 获取工程下拉框列表简要信息
    def get_proj_has_PDF_draw(self):
        url = self.builder + '/rs/pdfDrawingRest/getProjHasPdfDraw'
        resp = self.Webrequests.get(url,'',self.headers_builder).json()
        return resp

class DelDrawingInfos(CenterInterface):
    # 批量删除图纸
    def req_params(self,drawingId,ppid):
        params = [
              {
                "drawingId": drawingId,
                "ppid": ppid
              }
            ]
        return params

    def delete_drawing_infos(self,data):
        url = self.builder + '/rs/pdfDrawingRest/delDrawingInfos'
        resp = self.Webrequests.post_json(url,data,self.headers_builder).json()
        return resp
