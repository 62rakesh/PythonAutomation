import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class Locators():
    # Locators of Home page (Tc_1)
    Search_text = (By.ID, "twotabsearchtextbox")
    Search_submit = (By.XPATH, "(//INPUT[@class='nav-input'])[1]")
    # Locator of Product page (Tc_2)
    Product_detail = (By.XPATH, "(//IMG[@class='s-image'])[2]")
    # Locators of cart page (Tc_3)
    Add_to_cart = (By.ID, "add-to-cart-button")
    Sub_cart_page = (By.ID, "nav-cart")
    # Locators of Checkout page (Tc_4)
    Checkout_page = (By.XPATH, "(//INPUT[@type='submit'])[2]")
    # Locators of user login page (Tc_5)
    Enter_username = (By.ID, "ap_email")
    Submit_username = (By.XPATH, "(//INPUT[@id='continue'])")
    Enter_password = (By.XPATH, "(//INPUT[@id='ap_password'])")
    Submit_user = (By.XPATH, "(//INPUT[@id='signInSubmit'])")
