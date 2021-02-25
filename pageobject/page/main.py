#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register


class Main(BasePage):
    #继承了BasPage类 在子类重写了_base_url
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        #.index之前的.代表class
       self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
       return Register(self._driver)


    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self._driver)
