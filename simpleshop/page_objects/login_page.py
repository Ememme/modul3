from time import sleep
from simpleshop.tests.support_functions import *

from selenium.common.exceptions import StaleElementReferenceException

from simpleshop.tests.data_generator import *
user = '#username'
password = '#password'
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
error_info = '//*[@id="content"]/div/div[1]/ul'
# Test data
user1 = 'cotaga1249@maillei.net'
password1 = 'VRrMhK8MqFyd'

user2 = 'wowen49501@maillei.net'
password2 = 'lxsg#GAqH$Ke'

user3 = 'bomineg967@onmail3.com'
password3 = 'zedvu@##)CZy'

user4 = 'wacog70401@tinkmail.net'
password4 = 'Lk*3Q9&am3zL'

user5 = 'calose2528@maillei.net'
password5v= 'lkSb&SAJwLWo'


def correct_login(driver_instance):
    correct_user = driver_instance.find_element_by_css_selector(user)
    correct_user.send_keys(user1)
    correct_password = driver_instance.find_element_by_css_selector(password)
    correct_password.send_keys(password1)
    button = driver_instance.find_element_by_xpath(login_button)
    button.click()
    sleep(1)


def incorrect_login(driver_instance):
    incorrect_user = driver_instance.find_element_by_css_selector(user)
    incorrect_user.send_keys(DataGenerator.generateWrongEmail())
    incorrect_password = driver_instance.find_element_by_css_selector(password)
    incorrect_password.send_keys("test")
    button = driver_instance.find_element_by_xpath(login_button)
    button.click()
    sleep(1)
    try:
        wait_for_visibility_of_element(driver_instance, error_info)
        return button.is_displayed()
    except StaleElementReferenceException:
        print('ERROR: wrong user/password')
        return True




