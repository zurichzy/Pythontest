#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(params=[("tom",1213),('merry',234)])
def login(request):
    return  request.param

def test_case1(login):
    print(f"username:{login[0]},password:{login[1]}")
    print("case1")