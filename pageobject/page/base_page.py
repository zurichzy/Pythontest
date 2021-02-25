#!/usr/bin/env python
# -*- coding: utf-8 -*-

#公用 被调用的类
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
class  BasePage:
    _base_url = ""
    def __init__(self,driver:WebDriver=None):
        self._driver =""
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self._driver =driver
        if self._base_url !="":
            self.driver.get(self._base_url)

    def find(self,by,locator):
        return self.driver.find_element(by,locator)
