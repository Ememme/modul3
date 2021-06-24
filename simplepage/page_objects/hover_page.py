from simplepage.tests.helpers.support_functions import *

hovers_tab = 'hovers-header'
hovers_content = 'hovers-content'
hover_figure_1 = '//*[@id="hovers-content"]/div/div[1]'
hover_figure_1_link = '//*[@id="hovers-content"]/div/div[1]/div/a'


def click_hovers_tab(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, hovers_tab)
    element = driver_instance.find_element_by_id(hovers_tab)
    element.click()

def is_hover_content_displayed(driver_instance):
    element = wait_for_visibility_of_element_ID(driver_instance, hovers_content)
    return element.is_displayed()

def hover_over_and_click(driver_instance):
    hover_over_element(driver_instance, hover_figure_1)
    element = driver_instance.find_element_by_xpath(hover_figure_1_link)
    element.click()
