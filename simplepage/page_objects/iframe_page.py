from simplepage.tests.helpers.support_functions import *
from time import sleep
iframe_tab = '#iframe-header'
iframe = '#iframe-content > div > div > iframe'


def click_iframe_tab(driver_instance):
    tab = driver_instance.find_element_by_css_selector(iframe_tab)
    tab.click()
    sleep(2)


def is_iframe_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, iframe_tab)
    iframe_content = driver_instance.find_element_by_css_selector(iframe)
    return iframe_content.is_displayed


def find_buttons(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, iframe)
    driver_instance.switch_to.frame(0)
    buttons = driver_instance.find_elements_by_tag_name('button')

    checked_buttons = []
    for item in buttons:
        item.click()
        sleep(1)
        text = driver_instance.find_element_by_css_selector('#whichButtonIsClickedMessage')
        message = text.get_attribute('textContent')
        if item.text[-1] in message:
            # print(message)
            checked_buttons.append([item.text, True])
        else:
            checked_buttons.append([item.text, False])

    # print(checked_buttons)
    return all(checked_buttons)


