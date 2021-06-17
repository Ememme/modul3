from simplepage.tests.helpers.support_functions import *
from time import sleep

drag_and_drop_tab = '#draganddrop-header'
drag_content = '#draganddrop-content'


def click_drag_and_drop_tab(driver_instance):
    tab = driver_instance.find_element_by_css_selector(drag_and_drop_tab)
    tab.click()
    sleep(2)


def is_drag_drop_content_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, drag_content)
    content = driver_instance.find_element_by_css_selector(drag_content)
    return content.is_displayed()