import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from Resources.Locators import Locators
from Resources.TestData import TestData


class BasePage():
    # This function is called every time a object of the base class is created
    def __init__(self, driver):
        self.driver = driver

    # This function perform click on web element whose locator is passed to it
    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # This function perform the enter text into any input field
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def search(self):
        self.driver.find_element(*Locators.Search_text).clear()
        self.enter_text(Locators.Search_text, TestData.search_item)
        self.click(Locators.Search_submit)


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.Product_detail)


class AddToCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def Add_To_Cart(self):
        self.click(Locators.Add_to_cart)


class SubCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def View_Sub_Cart(self):
        self.click(Locators.Sub_cart_page)


class CheckOutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_Add_To_Cart(self):
        self.click(Locators.Add_to_cart)

