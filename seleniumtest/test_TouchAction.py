#!/usr/bin/env python
# -*- coding: utf-8 -*-


#脚本有问题

import time
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search= self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        #拖拽
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el,0,10000).perform()






