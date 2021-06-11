import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from simplepage.config.test_settings import TestSettings
from simplepage.page_objects import main_page, checkboxes_page, hover_page, users_page, inputs_page, drop_down_page, add_remove_element, date_picker_page


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

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes_tab_visible(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.is_checkbox_tab_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers_tab_visibility(self):
        hover_page.click_hovers_tab(self.driver)
        self.assertTrue(hover_page.is_hover_content_displayed(self.driver))
        hover_page.hover_over_and_click(self.driver)
        self.assertTrue(users_page.is_error_info_displayed(self.driver))

    def test4_input_tab_visibility(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.is_input_field_displayed(self.driver))

    def test5_send_correct_input_data(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_input_data(self.driver))

    def test6_send_incorrect_input_data(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_input_data(self.driver))

    def test7_dropdown_select(self):
        drop_down_page.click_dropdown_tab(self.driver)
        self.assertTrue(drop_down_page.is_dropdown_content_visible(self.driver))
        drop_down_page.get_dropdown_item(self.driver)

    def test8_add_remove_tab_visibility(self):
        add_remove_element.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_element.is_add_remove_content_visible(self.driver))

    def test9_add_element(self):
        add_remove_element.click_add_remove_tab(self.driver)
        add_remove_element.click_add_button(self.driver)
        self.assertTrue(add_remove_element.is_element_visible(self.driver))

    def test10_delete_element(self):
        add_remove_element.click_add_remove_tab(self.driver)
        add_remove_element.click_add_button(self.driver)
        add_remove_element.click_delete_button(self.driver)
        self.assertTrue(add_remove_element.is_element_invisible(self.driver))

    def test11_date_picker_visibility(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.is_date_picker_visible(self.driver))

    def test12_date_picker_template_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.check_template_date(self.driver))

    def test12_enter_correct_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.enter_correct_date(self.driver))

    def test13_enter_incorrect_date_string(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.enter_incorrect_date_string(self.driver))

    def test14_enter_incorrect_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.enter_incorrect_date_number(self.driver))

    def test15_enter_incorrect_min_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.enter_incorrect_min_date(self.driver))

    def test15_enter_incorrect_max_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.enter_incorrect_max_date(self.driver))

    #
    # def test16_pick_date(self):
    #     date_picker_page.click_date_picker_tab(self.driver)
    #     date_picker_page.pick_date(self.driver)

    if __name__ == '__main__':
        unittest.main()