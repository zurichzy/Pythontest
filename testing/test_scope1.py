#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
fixture的都可以放到conftest里面
'''

def test_case1(connDB):
    print("test_case1")

class TestDemo2:
    def test_a(self,connDB):
        print("test_a")

    def test_b(self,connDB):
        print("test_b")

class TestDemo3:
    def test_a(self,connDB):
        print("test_a")

    def test_b(self,connDB):
        print("test_b")