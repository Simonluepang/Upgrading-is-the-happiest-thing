#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pytest

def put_num():
    return 123123123132

@pytest.fixture(params=[put_num()])
def innerfunction(request):
    return request.param

class TestPytest():
    def assertEqual(self,innerfunction):
        my_function = innerfunction
        print(my_function)
        assert 0

def simple_gen():
    yield 1
    yield 23
    yield 56

def get_primes():
    num = 0
    while num <= 10:
        yield num
        num += 1
def make_list():
    idlist = []
    nextid = 1111
    for i in range(3):
        nextid += 1111
        idlist.append(nextid)
    return idlist

import random
def get_data():
    # 返回0~9之间的三个随机数
    return random.sample(range(10),4)

def consume():
    # 显示每次传入的整数列表的动态平均值
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        result = running_sum / float(data_items_seen)
        print(f'The running average is {result}')

def produce(condumer):
    # 产生序列集合，传递给消费函数
    while True:
        data = get_data()
        print(f"Produce{data}")
        condumer.send(data)
        yield


if __name__ == '__main__':
    # pytest.main(['test_pytest_sta.py'])
    # print(make_list())
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print("Producing...")
        next(producer)


    pass