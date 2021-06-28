import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from simpleshop.config.test_settings import TestSettings
from simpleshop.page_objects import main_page

class Test(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test1_main_page_visibility(self):
        main_page.is_content_visible(self.driver)