import unittest
import time
from time import sleep
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.BaseClass import BasePage, HomePage, SearchResultPage
from PageObjects.BaseClass import AddToCartPage
from PageObjects.BaseClass import SubCartPage
from Resources.Locators import Locators
from Resources.TestData import TestData

import os, sys, inspect

# fetch path to the directory in which current file is, from root directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Extract the path to parent directory
parentdir = os.path.dirname(currentdir)
#  insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir + '\Resources')
sys.path.insert(0, parentdir + '\PageObjects')


# from PageObjects.BaseClass import BasePage, HomePage
# from Resources.Locators import Locators
# from Resources.TestData import TestData


class Amazon_Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        # self.driver.quit()


class Test_Amazon_search(Amazon_Search):
    # super().__init__().setUp()
    def test_home_page_loaded(self):
        self.homepage = HomePage(self.driver)
        self.assertIn(TestData.home_title, self.homepage.driver.title)
        print(self.driver.title)

    def test_user_should_be_able_to_search(self):
        self.homepage = HomePage(self.driver)
        self.homepage.search()
        # self.homepage.driver.sleep(5)
        self.searchproduct = SearchResultPage(self.homepage.driver)
        self.searchproduct.click_search_result()
        # self.assertIn(TestData.search_item, self.searchproduct.driver.title())
        print(self.driver.title)

    def test_user_should_able_to_add_product_to_cart(self):
        self.homepage = HomePage(self.driver)
        self.homepage.search()
        # self.homepage.driver.sleep(5)
        self.searchproduct = SearchResultPage(self.homepage.driver)
        self.searchproduct.click_search_result()
        # self.assertIn(TestData.search_item, self.searchproduct.driver.title())
        # print(self.driver.title)
        self.searchproduct.driver.switch_to.window(self.searchproduct.driver.window_handles[1])
        # print(self.driver.title)
        self.Addproduct = AddToCartPage(self.searchproduct.driver)
        self.Addproduct.Add_To_Cart()
        print(self.driver.title)

    def test_user_should_go_to_the_sub_cart_page(self):
        self.homepage = HomePage(self.driver)
        self.homepage.search()
        # self.homepage.driver.sleep(5)
        self.searchproduct = SearchResultPage(self.homepage.driver)
        self.searchproduct.click_search_result()
        # self.assertIn(TestData.search_item, self.searchproduct.driver.title())
        # print(self.driver.title)
        self.searchproduct.driver.switch_to.window(self.searchproduct.driver.window_handles[1])
        # print(self.driver.title)
        self.Addproduct = AddToCartPage(self.searchproduct.driver)
        self.Addproduct.Add_To_Cart()
        print(self.driver.title)
        self.sub_cart = SubCartPage(self.Addproduct.driver)
        self.sub_cart.View_Sub_Cart()
        print(self.driver.title)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D://Python_Workspace//Amazon//Reports"))
