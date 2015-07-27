__author__ = 'muvaeva'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()


def element_exists(locator_type, locator_information):
    try:
        driver.find_element(locator_type, locator_information)
        return True
    except NoSuchElementException:
        return False


def element_visible(locator_type, locator_information):
    try:
        element = driver.find_element(locator_type, locator_information)
        return element.is_displayed()
    except NoSuchElementException:
        return False


driver.get("http://www.ebay.com/")
print(element_exists('id', 'gh-ac'))
print(element_visible('css', 'hide'))