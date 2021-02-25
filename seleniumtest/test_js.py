#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import  pytest
from seleniumtest.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://ww.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        time.sleep(3)

        # for code in [
        #     'return document.title','JSON.stringify(performance.timing)'
        # ]:
        print(self.driver.execute_script( 'return document.title ;return JSON.stringify(performance.timing)'))

    #修改1230的出发日期
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script(" a= document.getElementById('train_date');a.removeAttribute('readnoly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(2)
