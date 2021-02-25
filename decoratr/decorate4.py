#被装饰函数有参数的情况

import time
def time_1(time_2): #最外层管理，装饰器的参数
    def func1(aaaa):#管理传入的函数对象
        def func2(m_time):#最内层管理装饰器函数的参数
            if time_1:
                print('开始时间为',time.strftime('%S'))
                aaaa(m_time)
                print('结束时间为', time.strftime('%S'))
                #代表传入的函数对象被调用

            else:
               aaaa(m_time)
        return func2
    return  func1

@time_1(time_2 = True)
def be_decorate(m_time):
    time.sleep(m_time)
    print('被装饰的函数')

f1 = time_1(time_2=True) #返回func1函数对象
f2 = f1(be_decorate) #相当于func1（） --返回func2的函数对象
f2(3)
