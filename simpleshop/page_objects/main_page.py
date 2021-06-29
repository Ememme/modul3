from simplepage.tests.helpers.support_functions import *
from time import sleep

main_page_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_page_link_header = '#menu-item-100'
my_cart_page_link_header = '#menu-item-99'

def is_content_visible(driver_instance):
    logo = wait_for_visibility_of_element(driver_instance, main_page_logo)
    return logo.is_displayed()

def go_to_login_page(driver_instance):
    login = driver_instance.find_element_by_css_selector(my_account_page_link_header)
    login.click()
    sleep(1)
