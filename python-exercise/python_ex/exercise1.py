
#序列遍历时，会打印位置和对应的值
for i,v in enumerate(['tip','qianxi','liying']):
    print(i,v)

#字典遍历时，关键字和对应的值可以通过items()方法同时解读出来
ki = {'name':'qianxi','geder':'nan'}
for k,v in ki.items():
    print(k,v)

#list[]和tuple()很像，元组不可以修改没有append() and insert()方法
#能用tuple()代替list[]就尽量用tuple,不能修改代码安全
#定义一个元素，需要在元素后边加逗号
tuple = (1,)

l = []
for i in range(1,100):
    l.append(i)
print(l)
print(l[:10:2])
print(l[::5])

#生成列表
list=list(range(1, 11))

#列表生成式
l1 = [x*x for x in range(1,11)]
print(l1)

#使用两层循环，生成全排列
l2 = [n+m for n in 'ABC' for m in 'XYZ']
print(l2)

