#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class TestData:
    @pytest.mark.parametrize("a","b")
    def test_data1(self):
        a=10
        b=20
        print(a+b)

    # def test_data2(self):
    #     a=10
    #     b=20
    #     print(a+b)
    #
    # def test_data3(self):
    #     a=10
    #     b=20
    #     print(a+b)