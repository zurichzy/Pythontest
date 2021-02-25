import allure

@allure.link("http://www.baidu.com")
def test_with_link():
    print("这是一条加了连接的测试")
    pass

