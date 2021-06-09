from simplepage.tests.helpers.support_functions import *
from time import sleep


date_picker_tab = 'datepicker-header'
date_input = '//*[@id="start"]'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def is_date_picker_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, date_input)
    data_input = driver_instance.find_element_by_xpath(date_input)
    sleep(1)
    return data_input.is_displayed()
