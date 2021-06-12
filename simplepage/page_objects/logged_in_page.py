from simplepage.tests.helpers.support_functions import *

login_info = '//*[@id="loggedInMessage"]'


def is_logged_in_info_displayed(driver_instance):
    logged = wait_for_visibility_of_element(driver_instance, login_info)
    return logged.is_displayed()


def is_url_changed(driver_instance):
    redirected = driver_instance.current_url
    return redirected
