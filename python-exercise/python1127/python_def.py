

#函数作用：封装
#
# def func1(a):
#     """
#     函数的作用
#     :param a: 参数a的解释
#     :return:
#     """
#     print(a)
#     return 'a' #函数结束 print(a)
#
# func = lambda x: x*2
# print(func(2))

#
# list_hogwarts = [1,2,3]
# list_hogwarts.append(0)
# print(list_hogwarts)

#remove根据值删除
#pop根据索引删除
list_range =[]
for i in range(1,4):
    list_range.append(i**2)
print(list_range)

#推导式
list_range1 =[i**2 for i in range(1,4)]
print(list_range1)

list_square =[ i**2 for i  in range(1,4) if i!=1]
print(list_square)

list_square1 =[]
for  i in range(1,4):
    for j in range(1,4):
        list_square1.append(i*j)
print(list_square1)

list_square2 =[ i*j for i in range(1,4) for j in range(1,4)]
print(list_square2)


#list可变，tuple不可变，但是tuple里面的list可以变
a = [1,2,3,4,'a']
tuple_hog1 = (1,2,a)
tuple_hog1[2][0]= 'a'
print(tuple_hog1)
print(a.count('a'))

#集合

a ={1,2,3}
b = {1,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#集合去重功能
print({i for i in 'aaagdghdjehfkj'})


#字典,key不可变
a = {}
b= dict(a=1,b=2)


