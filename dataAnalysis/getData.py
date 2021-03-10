# coding=utf-8
# @Time : 2021/3/5 22:32 
# @Author : SeafyLiang 
# @Version：V 0.1
# @File : getData.py
# @desc : 获取数据

# 引入依赖 WEB自动化工具
from selenium import webdriver

# 初始化浏览器
driver = webdriver.Chrome("安装路径")
driver.get("http")
str1="xxx"
TCase = driver.find_element_by_xpath(str1)
print(TCase)
