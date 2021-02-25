#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 pytest test_fixture.py  --setup-show --setup teardown 操作
当一个方法上面加一个@pytest.fixture()装饰器就变成了fixture方法
yield能够激活fixture teardown 操作，yield 相当于return
yield前面的操作 相当于setup操作，yield语句后面相当于teardown操作
如果需要返回值，yield相当与return直接写在yield后面即可
'''
#autuuse可以应用到所有的测试用例中，不需要传入fixture参数
#如果需要返回数据 则需要传入fixture参数传到测试用例中

import pytest
@pytest.fixture(autouse=True)
def login():
    print('登录')
    username= 'tom'
    password = 12345
    #return [username,password]
    yield [username,password]
    print("登出")

def test_case1(login):
    print(f"测试用例1，需要登录{login}")

def test_case2():
    print("测试用例2")

def test_case3(login):
    print(f"测试用例3--需要登录 {login}")

@pytest.mark.usefixtures('login')
def test_case4(login):
    print("测试用例4")
    print(login)

