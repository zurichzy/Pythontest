# a=0
# if a==0:
#     print('a=0')
# else:
#     print("a!=0")

#1-100偶数求和
# result = 0
# for i in range(2,101,2):
#     result = result+i
# print(result)

# for i in range(1,10):
#     if i==5:
#         #跳出当前循环
#         continue
#     print(i)


import  random
computer_num = random.randint(1,20)
while True:
    person_num = int(input("请输入数字"))
    if person_num > computer_num:
        print("小一点")
    elif person_num<computer_num:
        print("大一点")
    elif person_num==computer_num:
        print("猜对了")
        break



