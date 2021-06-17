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


# Simulate drag and drop js code from: https://github.com/bormando/seleniumdad/blob/main/fixed.py
def drag_element(driver_instance):
    driver_instance.maximize_window()
    source = driver_instance.find_element_by_id('column-a')
    target = driver_instance.find_element_by_id('column-b')

    js_file = open("./../tests/helpers/simulate_drag_and_drop.js", "r")
    script = js_file.read()
    js_file.close()
    sleep(3)
    driver_instance.execute_script(script, source, target)
    sleep(1)
    header_value = driver_instance.find_element_by_tag_name('header').get_attribute('innerText')

    if header_value == 'B':
        return True
    else:
        return False
