import pytest
import yaml

from python_code.calculator import Calculator


 # def get_datas():
 #     with open('./datas/calc,yaml',encoding ='utf-8') as f:
 #         mydatas = yaml.safe_load(f)
 #         adddatas = mydatas['add']['datas']
 #         myids = mydatas['add']['myids']
 #    return [adddatas]


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',[
                             (1,2,3),
                             (100, 200, 300),
                             (0, 10, 10),
                             (-1,-2,-3),

                            ], ids=['整数','大整数','另相加','负数'])
    def test_add(self,a,b,expect):
        '''
        测试相加
        :return:
        '''
        print("测试相加")
       # calc = Calculator()
        result = self.calc.add(a,b)
        assert expect==result


    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2),
        (0.1, 0.2, 0.3),
    ])
    def test_add_float(self, a, b, expect):
        result = round(self.calc.add(a, b), 2)
        assert expect == result




