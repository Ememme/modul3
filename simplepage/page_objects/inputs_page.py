from simplepage.tests.helpers.support_functions import *

input_tab = '//*[@id="inputs-header"]'
input_field = '//*[@id="inputs-content"]/div/input'


def click_input_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_tab)
    element = driver_instance.find_element_by_xpath(input_tab)
    element.click()


def is_input_field_displayed(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, input_field)
    return element.is_displayed()


def send_correct_input_data(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_field)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('123456')
    value = 123456
    if value == int(elem.get_attribute("value")):
        return True
    else:
        return False

