#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# selenium
# https://selenium-python-zh.readthedocs.io/en/latest/
# https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

# from msilib.schema import Class
import requests  # http客户端模块
import time  # 日期时间模块
import pytest  # 单元测试模块
from selenium import webdriver
import allure
# from webdriver_init import * # 导入封装selenium初始化自定义模块
# from logging_init import * # 导入封装logging初始化自定义模块
import logging  # 日志模块
import pytesseract  # 验证码识别
import json
import webdriver_init
import logging_init
now_time = time.strftime("%Y-%m-%d %X")
# 初始化
driver = webdriver_init.DriverConfig.driver_config(webdriver)
# 初始化
logger = logging_init.LoggingConfig(
    logging, "./log/{}.txt".format(now_time)).logging_config()

'''
    [By类-可用属性]
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector

    [一次查找多个元素 (这些方法会返回一个list列表)]:

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector
'''


# 每个模块（文件）之前执行
def setup_module():
    logger.info("setup_module():每个模块（文件）之前执行")

# 每个模块（文件）之后执行


def teardown_module():
    driver.close()
    logger.info("teardown_module():每个模块（文件）之后执行")

# 每个类之前执行


def setup_class():
    logger.info("setup_class():每个类之前执行")

# 每个类之后执行


def teardown_class():
    logger.info("teardown_class():每个类之后执行")

# 每个方法之前执行


def setup_function():
    logger.info("setup_function():非类中的方法，每个方法之前执行")

# 每个方法之后执行


def teardown_function():
    logger.info("teardown_function():非类中的方法，每个方法之后执行")

# 类中的方法，每个方法之前执行


def setup_method():
    logger.info("setup_method():类中的方法，每个方法之前执行")

# 类中的方法，每个方法之后执行


def teardown_method():
    logger.info("teardown_method():类中的方法，每个方法之后执行")

@allure.feature("测试场景1")# # [标记主要功能]
class Test_01():
    '''
        DDT 数据驱动（参数化）
    '''
    # 参数化数据
    data = [("http://www.baidu.com", "百度搜索"), ("http://www.bing.com", "必应搜索")]
    @pytest.mark.parametrize("url,search_text", data)
    @pytest.mark.L1
    @pytest.mark.test
    @allure.story("测试用例1-1")# [标注Feature功能模块下的分支功能]
    @allure.severity(" blocker")# [标记测试用例等级] blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）;critical级别：临界缺陷（功能点缺失）;normal级别：正常 默认为这个级别;minor级别：次要缺陷（界面错误与UI需求不符）;trivial级别：轻微缺陷（必输项无提示，或者提示不规范） 
    @allure.description("描述用例信息")
    def test_baidu_search(self, url, search_text):
        driver.maximize_window()# 窗口最大化
        driver.get(url) #打开网页
        try:
            if("baidu" in url):
                driver.find_element_by_id("kw").send_keys(search_text)# 输入
                driver.find_element_by_id('su').click()# 点击
            elif("bing" in url):
                driver.find_element_by_id("sb_form_q").send_keys("python")
                driver.find_element_by_id('search_icon').click()
        except(ValueError):
            print(ValueError)
        time.sleep(10)
        # 截图-输出控制台
        file = driver.get_screenshot_as_png
        logger.info(file)
        # 截图-保存本地
        self.save_screenshot()
        logger.info("测试数据为{}".format(url))
        logger.info("测试数据为{}".format(search_text))

    '''
        跳过的测试用例c
    '''
    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.step("这是一个步骤")# [标注测试用例的重要步骤]
    @allure.testcase("https://home.cnblogs.com/","测试用例地址请点击跳转")     #标记代码，你可以指定连接的名字，报告里面就会现在这个名字的连接
    @allure.issue("http://www.baidu.com") #标记代码，哪个写在后，在报告里面就会显示在前面
    def test_bing_search(self):
       try:
            driver.maximize_window()
            url = "http://www.bing.com"
            driver.get(url)
            driver.find_element_by_id("sb_form_q").send_keys("python")
            driver.find_element_by_id('search_icon').click()
            time.sleep(2)
            # 截图-输出控制台
            file = driver.get_screenshot_as_png
            logger.info(file)
       except Exception as e:
            logger.error("报错：{}".format(e))
            # 截图-保存本地
            self.save_screenshot()

    '''
        selenium 截图保存本地
    '''

    def save_screenshot(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        if driver.get_screenshot_as_file('./save_images/%s.png' % now_time):
            logger.info('保存成功')
        else:
            logger.info('保存失败')
if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','./report/'])
    
    '''
    [参数说明]
    "-m": 标记用例
    "login": 被标记需要执行用例
    "-s":允许终端在测试运行时输出某些结果，例如你想输入print的内容，可以加上-s
    "-q":简化输出结果
    "--alluredir": 生成allure指定语法
    "./report":生成报告的路径
    "--clean-alluredir":因为这个插件库allure-pytest生成的报告文件，你第二次运行时候不会清理掉里面的东西，所以你需要删除这个report文件夹，然后运行重新新建reoprt文件夹
    说明:运行后，会在report文件夹里面生成文件
    '''