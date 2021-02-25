#!/usr/bin/env python
# -*- coding: utf-8 -*-

# str='124739574985'
# print(str[::-1])
#
# l=list(str)
# l.reverse()
# print(''.join(l))
#
# li = [1, 2, 10, 10, 2, 1]
# print([v for v in li if v == max(li)])

# sxh = []
# for i in range(100, 1000):
#     s = 0
#     for j in str(i):
#         s += int(j)**3
#     if i == int(j)**3:
#         sxh.append(i)
# print(sxh)

def func(*argc):
    lens = len(*argc)
    count = 0
    tup=argc[0]  #取出参数元组
    for i in range(0,lens-1):
        for j in range(i+1,lens):
            if(tup[i] > tup[j]):
                count += 1
    return count
list = [7,5,6,4]

print(func(list))