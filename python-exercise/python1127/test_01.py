# try:
#     num1 = int(input("输入一个数"))
#     num2 = int(input("输入一个被除数"))
#     print(num1/num2)
# except :
#     print("这是一个异常")
# finally:
#     print("无论有没有异常，都执行")

#
#
# x =10
# if x >5:
#     raise Exception("这是一个异常")
class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
raise MyException("value1","value2")



