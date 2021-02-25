#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActions:
    def setup(self):
        self.driver  = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

