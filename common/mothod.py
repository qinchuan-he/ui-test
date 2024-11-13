from selenium import webdriver
from common.driver import driver
from selenium.webdriver import ActionChains
import time

class Mothed():

    def __init__(self):
        print('----------------method-----')
        self.driver = driver()

    def by_path(self, element):
        return self.driver.find_element_by_xpath(element)

    def send_keys(self, element, value):
        self.driver.find_element_by_xpath(element).send_keys(value)

    def click(self, element):
        self.driver.find_element_by_xpath(element).click()

    def sleep(self,value):
        time.sleep(value)

    def moveto(self,element):
        ActionChains(driver).move_to_element(self.by_path(element))
