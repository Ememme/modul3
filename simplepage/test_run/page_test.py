import unittest
from selenium import webdriver
from simplepage.config.test_settings import TestSettings
from simplepage.page_objects import main_page, checkboxes_page


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checboxes_tab_visible(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.is_checkbox_tab_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)