from os import path
from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    封装常用的selenium方法
    """

    def __init__(self, browser_type=None):
        """
        打开浏览器
        :param browser_type:
        """
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome(u'D:\Python代码\selenium\cases\chromedriver.exe')
        elif browser_type == 'firefox':
            path ='D:/Python代码/selenium/page/geckodriver.exe'
            self.driver = webdriver.Firefox()
        elif browser_type == 'safari':
            self.driver = webdriver.Safari()
        elif browser_type == 'opean':
            self.driver = webdriver.Opera()
        else:
            raise NameError("浏览器类型输入错误")

    def navigate(self, url):
        # 打开浏览器
        self.driver.get(url)

    def _find_element(self, element):
        if '=>' not in element:
            return self.driver.find_element_by_id(element)

        by = element.split('=>')[0].strip()
        value = element.split('=>')[1].strip()

        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'link':
            element = self.driver.find_element_by_link_text(value)
        else:
            raise NameError("元素定位方式错误, 请输入id,name,class,css,xpath,link进行定位")
        return element

    def input(self, element, text):
        """
        输入文本
        :param element: 元素定位
        :param text: 输入的文本内容
        :return: 无
        """
        self._find_element(element).clear()        # 清空输入框
        self._find_element(element).send_keys(text) # 输入

    def click(self, element):
        """
        点击
        :param element: 元素定位
        :return: 无
        """
        self._find_element(element).click()

    def select_by_index(self, element, index):
        """
        下拉框选择（通过index方式定位）
        :param element: 元素定位
        :param index: 0 表示第一个下拉框
        :return: 无
        """
        ele = self._find_element(element)
        Select(ele).select_by_index(index)

    def select_by_value(self, element, value):
        """
        下拉框选择（通过value方式定位）
        :param element:
        :param value:
        :return:
        """
        ele = self._find_element(element)
        Select(ele).select_by_value(value)

    def select_by_vis_text(self, element, text):
        """
        下拉框选择（通过可视化文本方式定位）
        :param element: 元素定位
        :param text: 下拉框的文本
        :return: 无
        """
        ele = self._find_element(element)
        Select(ele).select_by_visible_text(text)

    def uploda(self, element, file):
        """
        上传（input）标签
        :param element: 元素定位
        :param file: 上传文件
        :return: 无
        """
        upload = self._find_element(element)
        upload.send_keys(file)

    def sleep(self, time):
        """
        等待时间
        :param time:
        :return:
        """
        sleep(time)

    def quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def max_windows(self):
        self.driver.maximize_window()

