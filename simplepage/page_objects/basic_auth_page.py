from simplepage.tests.helpers.support_functions import *
from time import sleep


basic_auth_tab = '#basicauth-header'
basic_auth = '#basicauth-content'
username_input = '#ba_username'
password_input = '#ba_password'
login_button = '#content > button'



def click_basic_auth_tab(driver_instance):
    tab = driver_instance.find_element_by_css_selector(basic_auth_tab)
    tab.click()
    sleep(1)


def is_basic_auth_content_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, basic_auth)
    basic_auth_content = driver_instance.find_element_by_css_selector(basic_auth)
    return basic_auth_content.is_displayed()


def send_correct_username_and_password(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, basic_auth)
    user_login = driver_instance.find_element_by_css_selector(username_input)
    user_password = driver_instance.find_element_by_css_selector(password_input)
    button = driver_instance.find_element_by_css_selector(login_button)
    user_login.send_keys('admin')
    user_password.send_keys('admin')
    button.click()
    sleep(2)




