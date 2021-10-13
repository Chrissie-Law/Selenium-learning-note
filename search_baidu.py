#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/10/11 22:56
# @Author  : ChrissieLaw
# @File    : search_baidu.py
# @Software: PyCharm
# @Function:
"""

from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'D:\MyProgromFiles\webdrivers\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element_by_id('kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 法1，比如输入字符串到 这个 输入框里,加回车
# element.send_keys('icdm\n')

# 法2，输入后点击
element.send_keys('icdm')
element = wd.find_element_by_id('su')
element.click()