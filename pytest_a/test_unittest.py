'''
单元测试框架
'''



import unittest
#unittest.TestCase 固定写法
class TestStringMethods(unittest.TestCase):
    #setUp 和tearDown 方法是在每条测试用例前后分别调用的方法
    def setUp(self) -> None:  #默认返回值是none
        print('setup')

    def tearDown(self) -> None:
         print('tearDown')

      #setUpClass 和tearDownClass 是在整个类的前后分别调用
    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()












