import yaml
import pytest
class TestData:
    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data_yaml")))
    def test_data(self,a,b):
        print(a+b)
