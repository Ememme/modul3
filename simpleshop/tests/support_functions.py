from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from time import sleep


def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=2):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_ID(driver_instance, id, time_to_wait=2):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element_xpath(driver_instance, xpath, time_to_wait=8):
    inv_elem = WebDriverWait(driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem


# Function to convert date from format: YYYY-MM-DD to DD-MM - used in DatePicker
def convert_date_format(date):
    month_day_date = date[8:] + "-" + date[5:7]
    return month_day_date


# Function used in KeyPresses
def iterate_over_dictionary(driver_instance, dictionary, input_id, result_id):
    input = driver_instance.find_element_by_css_selector(input_id)
    result = driver_instance.find_element_by_css_selector(result_id)
    errors = []

    for key, value in dictionary.items():
        input.send_keys(value)
        sleep(.5)
        displayed = result.get_attribute('textContent').split("You entered: ", 1)[-1]
        # print(value, displayed)
        if len(displayed) == 0:
            errors.append([key, result.get_attribute('textContent')])
    return errors