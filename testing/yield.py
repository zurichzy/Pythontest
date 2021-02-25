#!/usr/bin/env python
# -*- coding: utf-8 -*-

#yield Python生成器,如果衣蛾方法使用了yield，这个方法就变成了生成器

def prodiver():
    for i in range(1,10):
       yield  i #相当于return i，同时记录下当时执行的位置

p = prodiver()
print(next(p))
print(next(p))
