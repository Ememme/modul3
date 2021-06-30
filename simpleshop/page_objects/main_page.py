from simplepage.tests.helpers.support_functions import *
from time import sleep

main_page_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_page_link_header = '#menu-item-100'
my_cart_page_link_header = '#menu-item-99'
cart_in_header = '#site-header-cart'
add_hoodie_to_cart_button = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a'
go_to_cart_under_item_button = '//*[@id="post-83"]/div/div[3]/ul/li[3]/div[2]/a[2]'


def is_content_visible(driver_instance):
    logo = wait_for_visibility_of_element(driver_instance, main_page_logo)
    return logo.is_displayed()


def go_to_login_page(driver_instance):
    login = driver_instance.find_element_by_css_selector(my_account_page_link_header)
    login.click()
    sleep(1)


def add_item_to_cart(driver_instance):
    item = driver_instance.find_element_by_xpath(add_hoodie_to_cart_button)
    item.click()
    sleep(2)


def go_to_cart_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, go_to_cart_under_item_button)
    button = driver_instance.find_element_by_xpath(go_to_cart_under_item_button)
    button.click()
    sleep(1)