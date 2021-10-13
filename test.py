#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/10/11 11:15
# @Author  : ChrissieLaw
# @File    : test.py
# @Software: PyCharm
# @Function:
"""

from selenium import webdriver

#  创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'D:\MyProgromFiles\webdrivers\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://www.baidu.com')