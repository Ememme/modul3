from simplepage.tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

status_code_tab = '#statuscodes-header'


def click_status_code_tab(driver_instance):
    tab = driver_instance.find_element_by_css_selector(status_code_tab)
    tab.click()


def is_status_content_visible(driver_instance):
    tab = driver_instance.find_element_by_css_selector(status_code_tab)
    tab.click()
    sleep(3)
    return tab.is_displayed


def find_and_click_all_links(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, '#statuscodes-content')
    links = driver_instance.find_elements_by_xpath("//a[contains(@href, '//httpstat.us/')]")
    main_window = driver_instance.window_handles[0]
    codes = []

    for link_el in links:
        status = link_el.text
        ActionChains(driver_instance).move_to_element(link_el).key_down(Keys.COMMAND).click(link_el).key_up(Keys.COMMAND).perform()
        driver_instance.switch_to.window(driver_instance.window_handles[1])
        status_url = driver_instance.current_url
        if status in status_url:
            codes.append([status, True])
        else:
            codes.append([status, False])
        driver_instance.close()
        driver_instance.switch_to.window(main_window)

    # print(codes)
    return all(codes)

