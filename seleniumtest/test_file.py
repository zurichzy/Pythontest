#!/usr/bin/env python
# -*- coding: utf-8 -*-
from seleniumtest.base import Base
from  time import sleep

class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_elements_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/sucuo/PycharmProjects/pythonProject/firsr_python/seleniumtest/img/cda0079e174161b94fe8342d130bf5d0.jpeg")
        sleep(2)


