#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
# list=[]
# for i in range(1,10):
#     list.append(i)
# print(list)

#随机生成10个数字，打印出最小的三个
result = random.sample(range(1,100),10)
print(result)
result.sort()
print(result[-3:])

