from simplepage.tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from time import sleep

dropdown_tab = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
droppdown_list = '//*[@id="dropdown"]'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dropdown_tab)
    elem.click()


def is_dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_ID(driver_instance, dropdown_content)
    return elem

def get_dropdown_item(driver_instance):
    dropdown_items = Select(driver_instance.find_element_by_xpath(droppdown_list))
    wait_for_visibility_of_element(driver_instance, droppdown_list, time_to_wait=1)
    dropdown_items.select_by_index(1)
    sleep(3)
