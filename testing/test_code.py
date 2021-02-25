import pytest

from python_code.calculator import Calculator

'''
pytest 命名规则
文件名：以test_开头（test_*.py）
类名：以Test开头
方法名：以test_开头

'''

class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',[
                             (1,2,3),
                             (0.1, 0.2, 0.3),
                             (100, 200, 300),
                             (0, 10, 10),
                             (-1,-2,-3),

                            ], ids=['int','float','bigint','zero','minus'])
    def test_add(self,a,b,expect):
        '''
        测试相加
        :return:
        '''
        print("测试相加")
       # calc = Calculator()
        result = self.calc.add(a,b)
        assert expect==result

    def test_add1(self):
        '''
        测试相加
        :return:
        '''
        print("测试相加1")
        #calc = Calculator()
        result = self.calc.add(0.1,0.1)
        assert 1 == result

    def test_add2(self):
        '''
        测试相加
        :return:
        '''
        print("测试相加")
        #calc = Calculator()
        result = self.calc.add(100, 100)
        assert 200 == result


    def test_div(self):
        '''
        测试相除
        :return:
        '''
        print("测试相除")
        #calc = Calculator()
        result =self.calc.div(100,2)
        assert 50==result


    def test_func(self):
        print('ceshi')

