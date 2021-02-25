import yaml

import pytest_a


class TestDemo:
    @pytest_a.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print('这是测试环境')
        elif  "dev" in env:
            print("这是开发环境")