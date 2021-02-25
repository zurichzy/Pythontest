#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# import pytest
#
# def test_success():
#     """this test succeeds"""
#     assert True
#
#
# def test_failure():
#     """this test fails"""
#     assert False
#
#
# def test_skip():
#     """this test is skipped"""
#     pytest.skip('for a reason!')
#
#
# def test_broken():
#     raise Exception('oops')


import allure
@allure.link("http://www.biadu.com",name='链接')
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = 'https://pdf.ceshiren.com/lg3/python-Pytest%E6%B5%8B%E8%AF%95%E5%AE%9E%E6%88%981/assets/player/KeynoteDHTMLPlayer.html#21'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条登录的测试用例")
    pass