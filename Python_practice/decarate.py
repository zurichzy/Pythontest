#!/usr/bin/env python
# -*- coding: utf-8 -*-

#闭包函数
#函数定义
def func1():
    #在函数func1内再定义一个函数
    def func2():
        print("我是func2")
        
    return func2()


#函数调用
func1()