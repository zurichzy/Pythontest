
#被测方法
import unittest
class Search:

    def search_fun(self):
        print('search')
        return  True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('class')


    def test_search1(self):
        print('search1')
        search  =Search()
        assert True == search.search_fun()

    def test_search2(self):
        print('search2')
        search  =Search()
        assert True == search.search_fun()

    def test_equal(self):
        print('断言相等')
        self.assertNotEqual(1,2,'panduan 1==2')

if __name__ == '__main__':
    unittest.main()
#创建一个
