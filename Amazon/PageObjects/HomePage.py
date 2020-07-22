from PageObjects.BaseClass import BasePage
from Resources.TestData import TestData
from Resources.Locators import Locators
import selenium
from selenium import webdriver


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def search(self):
        self.driver.find_element(*Locators.Search_text).clear()
        self.enter_text(Locators.Search_text, TestData.search_item)
        self.click(Locators.Search_submit)
