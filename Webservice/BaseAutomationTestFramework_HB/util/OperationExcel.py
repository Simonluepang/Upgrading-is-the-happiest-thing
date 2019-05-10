#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by hu on 2018/4/29

import xlrd

class OperationExcel:
    '''
    操作excel
    '''
    def __init__(self,fileName="2017年4月主管绩效表-开发2部-胡彪-20170323.xlsx",sheetID=0):
        '''
        :param fileName: excel文件路径
        :param sheetId: sheet ID
        '''
        self.fileName = fileName
        self.sheetID = sheetID
        self.data = self.get_data()

    def get_data(self):
        '''
        打开excel,获取指定sheet的数据
        :return: 返回sheet数据
        '''
        xl = xlrd.open_workbook(self.fileName)
        table = xl.sheet_by_index(self.sheetID)
        return table

    def get_lines(self):
        '''
        返回总行数
        :return:
        '''
        return self.data.nrows

    def get_cells(self):
        '''
        返回总列数
        :return:
        '''
        return self.data.ncols

    def get_line(self,rowx):
        '''
        返回指定行
        :return:
        '''
        return self.data.row(rowx)

    def get_cell(self,rowx,colx):
        '''
        返回指定列
        :return:
        '''
        return self.data.cell(rowx,colx)

if __name__ == '__main__':
    oper = OperationExcel()
    print(oper.get_data().nrows)
    print(oper.get_lines())
    print(oper.get_cells())
    print(oper.get_line(0))
    print(oper.get_cell(0,0))
