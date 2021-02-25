#!/usr/bin/env python
# -*- coding: utf-8 -*-
import selenium

from selenium import webdriver

from firsr_python.seleniumtest.base import Base


class Jiliang(Base):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://jjg.spc.org.cn/resmea/standard/JJF%25201856-2020/")
    driver.find_element_by_class_name("read").click()
    driver.find_element_by_class_name("disabled").click()
    driver.find_element_by_class_name("current").click()
    driver.quit()



