from simplepage.tests.helpers.support_functions import *

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


