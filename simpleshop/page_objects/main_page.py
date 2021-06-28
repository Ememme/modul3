from simplepage.tests.helpers.support_functions import *

main_page_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'


def is_content_visible(driver_instance):
    logo = wait_for_visibility_of_element(driver_instance, main_page_logo)
    return logo.is_displayed()