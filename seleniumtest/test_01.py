#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        pass

    def teardown(self):
        pass

    def test_wait(self):
        sleep(3)


'''

self.driver.implicitly_wait(3)


'''

