from simplepage.tests.helpers.support_functions import *
from time import sleep

add_remove_element_tab = 'addremoveelements-header'
add_remove_element_content = 'addremoveelements-content'
add_button = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_add_remove_tab(driver_instance):
    tab = driver_instance.find_element_by_id(add_remove_element_tab)
    tab.click()


def is_add_remove_content_visible(driver_instance):
    content = wait_for_visibility_of_element_ID(driver_instance, add_remove_element_content)
    sleep(3)
    return content.is_displayed()


def is_element_visible(driver_instance):
    delete_button = wait_for_visibility_of_element(driver_instance, added_element)
    return delete_button.is_displayed()


def click_add_button(driver_instance):
    button = wait_for_visibility_of_element(driver_instance, add_button)
    button.click()
    sleep(2)


def click_delete_button(driver_instance):
    delete_button = driver_instance.find_element_by_xpath(added_element)
    delete_button.click()
    wait_for_invisibility_of_element_xpath(driver_instance, added_element)
    sleep(2)


def is_element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False

