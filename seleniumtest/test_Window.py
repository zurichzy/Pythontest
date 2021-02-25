#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

from seleniumtest.base import Base
from time import  sleep
class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("usenmame")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13600000000")
        sleep(3)

        #switch_to_window() --进行窗口切换
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_name")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

