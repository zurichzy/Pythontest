#被装饰函数有参数的情况

import time
def func1(func):
    def func2(m_time):
        print('开始时间为',time.strftime('%S'))
        #代表传入的函数对象被调用
        func(m_time)

        print('结束时间为', time.strftime('%S'))
    return func2

@func1
def be_decorate(m_time):
    time.sleep(m_time)
    print('被装饰的函数')

be_decorate(3)
