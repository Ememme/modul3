from simplepage.tests.helpers.support_functions import *

error_info = 'container'


def is_error_info_displayed(driver_instance):
    element = wait_for_visibility_of_element_ID(driver_instance, error_info)
    return element.is_displayed()