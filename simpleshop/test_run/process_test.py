import unittest

from selenium import webdriver

from simpleshop.config.test_settings import TestSettings
from simpleshop.page_objects import main_page, login_page, account_page, cart_page, order_process_page


class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def test1_process(self):
        self.assertTrue(main_page.is_content_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.is_item_in_cart(self.driver))
        cart_page.submit_cart(self.driver)
        order_process_page.fill_all_valid_form_areas(self.driver)
        order_process_page.submit_order(self.driver)
