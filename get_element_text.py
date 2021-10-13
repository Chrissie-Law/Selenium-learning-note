#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/10/11 23:51
# @Author  : ChrissieLaw
# @File    : get_element_text.py
# @Software: PyCharm
# @Function:
"""
from selenium import webdriver

wd = webdriver.Chrome(r'D:\MyProgromFiles\webdrivers\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements_by_class_name('animal')

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)

pass