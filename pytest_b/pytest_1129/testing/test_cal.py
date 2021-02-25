import pytest

from pytest_b.pytest_1129.calculator import Calculator

#必须选择pytest来运行

'''
文件名：以test_开头（test*.py）
类名：以Test开头
方法名：以test_开头

'''
class TestCalc:
    @pytest.mark.ad
    def test_add(self):
        '''
        测试相加
        :return:
        '''
        calc = Calculator()
        result = calc.add(1,1,)
        assert 2  == result

    def test_add1(self):
        '''
        测试相加
        :return:
        '''
        calc = Calculator()
        result = calc.add(1, 1, )
        assert 3 == result

    def test_add2(self):
        '''
        测试相加
        :return:
        '''
        calc = Calculator()
        result = calc.add(1, 1, )
        assert 4== result

    def test_func(self):
        print('test')
