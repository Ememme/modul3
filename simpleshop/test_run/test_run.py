import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from simpleshop.config.test_settings import TestSettings
from simpleshop.page_objects import main_page, login_page, account_page


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
        self.assertTrue(main_page.is_content_visible(self.driver))

    def test2_go_to_login_page(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(account_page.is_account_visible(self.driver))

    def test3_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login(self.driver))



