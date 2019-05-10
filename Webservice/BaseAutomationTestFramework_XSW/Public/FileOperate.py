#coding=utf-8
import os
from Setting import *

def read_dynamic_generation_txt(path,match,splitSymbol=SpliteSymbol,lr=1):
    '''读取动态生成的txt文件，通过匹配到的行以及分隔符来获得需要的值'''
    value = ''
    with open(path, 'r') as f:
        for line in f.readlines():
            if match in line.split(splitSymbol)[0]:
                value = line.split(splitSymbol)[lr]
        return value.strip('\n')

# def read_dynamic_generation_txt(path,match,splitSymbol=SpliteSymbol,lr=1):
#     '''读取动态生成的txt文件，通过匹配到的行以及分隔符来获得需要的值'''
#     with open(path, 'r') as f:
#         for line in f.readlines():
#             if match in line:
#                 value = line.split(splitSymbol)[lr]
#                 print(1)
#                 return value.strip('\n')


def write_value_to_txt(path,name,value,splitSymbol=SpliteSymbol):
    with open(path, 'a+') as f:
        f.write(name + splitSymbol + value + os.linesep)







