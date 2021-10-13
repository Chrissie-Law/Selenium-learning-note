#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/10/12 0:09
# @Author  : ChrissieLaw
# @File    : get_search_result.py
# @Software: PyCharm
# @Function:
"""
from selenium import webdriver
import time
import chardet

def baidu_search():
    wd = webdriver.Chrome(r'D:\MyProgromFiles\webdrivers\chromedriver.exe')
    wd.implicitly_wait(10)  # 隐式等待时间

    wd.get('https://www.baidu.com')
    element = wd.find_element_by_id('kw')
    element.send_keys('icdm\n')

    list = wd.find_elements_by_class_name('c-container')
    for i in range(1, len(list)+1):
        element = list[i-1]
        abstract = element.text.split('')[0]
        if '其他人还在搜' not in abstract:
            # abstract = abstract.encode('utf-8')
            file.write('Result {}:\n'.format(i))
            file.write(abstract.encode('gbk','ignore').decode('gbk') )
            file.write('\n')
            # print(abstract)
            # print(chardet.detect(str.encode(abstract)))

    time.sleep(3)
    wd.close()


if __name__=='__main__':
    file = open('data.txt', 'w+')
    baidu_search()
    file.close()