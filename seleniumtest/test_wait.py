#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import sleep

from selenium import  webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
       # self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹学院")
        self.driver.find_element(By.ID,'su').click()

