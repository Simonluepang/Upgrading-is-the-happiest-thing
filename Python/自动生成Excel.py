#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt

def make_Excel_Data():

	book = xlwt.Workbook(encoding='utf-8', style_compression=0)

	sheet = book.add_sheet('隐患库', cell_overwrite_ok=True)

	TableHeadList = ['隐患要素','隐患类别','隐患内容','隐患说明']

	# 编写表头
	for i in range(4):
		sheet.write(0, i, TableHeadList[i])

	#编写内容
	for i in range(200):
		for u in range(2):
			sheet.write(i+1,u,TableHeadList[u]+"Test"+str(u))

	for i in range(200):
		for u in range(2):
			sheet.write(i+1,u+2,TableHeadList[u]+"Test"+str(i))


	book.save(r'E:\NewFile\Data200.xls')

make_Excel_Data()