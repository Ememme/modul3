from simplepage.tests.helpers.support_functions import *
from selenium.webdriver.common.alert import Alert
from time import sleep

form_tab = '#form-header'
form_content = '#form-content'
form_input_name = '#fname'
form_input_last_name = '#lname'
form_submit_button = '#formSubmitButton'


def click_form_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    element = driver_instance.find_element_by_css_selector(form_tab)
    element.click()


def is_form_content_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    content = driver_instance.find_element_by_css_selector(form_content)
    return content.is_displayed()


def send_correct_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    name_input = driver_instance.find_element_by_css_selector(form_input_name)
    name_input.send_keys('name')
    last_name_input = driver_instance.find_element_by_css_selector(form_input_last_name)
    last_name_input.send_keys('last name')
    submit_button = driver_instance.find_element_by_css_selector(form_submit_button)
    submit_button.click()
    alert_info_text = Alert(driver_instance).text
    print(alert_info_text)
    Alert(driver_instance).accept()
    return alert_info_text


def send_empty_inputs(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    name_input = driver_instance.find_element_by_css_selector(form_input_name)
    name_input.send_keys('')
    last_name_input = driver_instance.find_element_by_css_selector(form_input_last_name)
    last_name_input.send_keys('')
    submit_button = driver_instance.find_element_by_css_selector(form_submit_button)
    submit_button.click()
    first_name_validation_text = name_input.get_attribute("validationMessage")
    sleep(1)
    print(first_name_validation_text)
    return first_name_validation_text


def send_empty_input_last_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, form_tab)
    name_input = driver_instance.find_element_by_css_selector(form_input_name)
    name_input.send_keys('first name')
    last_name_input = driver_instance.find_element_by_css_selector(form_input_last_name)
    last_name_input.send_keys('')
    submit_button = driver_instance.find_element_by_css_selector(form_submit_button)
    submit_button.click()
    validation_text = last_name_input.get_attribute("validationMessage")
    sleep(1)
    print(validation_text)
    return validation_text

