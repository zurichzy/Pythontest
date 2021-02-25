
#模块级别，不属于任何一个类
def setup_module():
    print("setup_module:模块级别的A")

def teardown_module():
    print("teardown_module:模块级别A")

class TestA:
#setup_class. teardown_class 类级别 在每个类执行前后被调用
    def setup_class(self):
        print("class setup B")

    def teardown_class(self):
        print("class down B")

#setup teardown 是方法级别的 在每个类里面的测试用例前后分别被 调用一次
    def setup(self):
        print("setup:测试前的准备C")

    def teardown(self):
        print("teardown:测试用例后的资源释放C")

    def test_a(self):
        print("test_")

    def test_b(self):
        print("testb")

def setup_function():
    print("setup:函数级别")

def teardown_function():
    print("teardown:函数级别")