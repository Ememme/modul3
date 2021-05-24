from simplepage.tests.helpers.support_functions import *

checkbox_tab = '//*[@id="checkbox-header"]'
checkboxes_all = '//*[@id="checkboxes"]'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def is_checkbox_tab_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, checkboxes_all)
    print(elem)
    return elem.is_displayed()

def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, checkbox_tab)
    elem = driver_instance.find_element_by_xpath(checkbox_tab)
    elem.click()

def click_checkboxes(driver_instance):
    elem_1 = driver_instance.find_element_by_xpath(checkbox_1)
    elem_1.click()
    elem_2 = driver_instance.find_element_by_xpath(checkbox_2)
    elem_2.click()