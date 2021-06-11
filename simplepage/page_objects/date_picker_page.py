from simplepage.tests.helpers.support_functions import *
from time import sleep

date_picker_tab = 'datepicker-header'
date_input = '//*[@id="start"]'
date_calendar = 'input[type="date"]::-webkit-calendar-picker-indicator'
cal = '//*[@id="picker"]'

# FORMAT DATY DD/MM/YYYY

def click_date_picker_tab(driver_instance):
    date_tab = driver_instance.find_element_by_id(date_picker_tab)
    date_tab.click()


def is_date_picker_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, date_input)
    data_input = driver_instance.find_element_by_xpath(date_input)
    return data_input.is_displayed()


def check_template_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    elem = driver_instance.find_element_by_xpath(date_input)
    template_date = '2020-07-22'
    displayed_date = elem.get_attribute("value")
    print(template_date, displayed_date)

    if template_date == displayed_date:
        return True
    else:
        return False


def enter_correct_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    date = driver_instance.find_element_by_xpath(date_input)
    new_date = '10-11'
    date.send_keys(new_date)
    sleep(2)
    displayed_date = date.get_attribute("value")
    # print('Actual value: ' + displayed_date + ' expected value: ' + new_date)
    if convert_date_format(displayed_date) == new_date:
        return True
    else:
        return False


def enter_incorrect_date_string(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    date = driver_instance.find_element_by_xpath(date_input)
    new_incorrect_date = "string_data"
    date.send_keys(new_incorrect_date)
    sleep(1)
    displayed_date = date.get_attribute("value")

    if displayed_date != new_incorrect_date:
        return True
    else:
        return False


def enter_incorrect_date_number(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    date = driver_instance.find_element_by_xpath(date_input)
    new_incorrect_date = '99-99'
    date.send_keys(new_incorrect_date)
    sleep(1)
    displayed_date = date.get_attribute("value")
    print(new_incorrect_date, displayed_date)

    if convert_date_format(displayed_date) != new_incorrect_date:
        return True
    else:
        return False


def enter_incorrect_min_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    date = driver_instance.find_element_by_xpath(date_input)
    out_of_min_range_date = '31-12-1999'
    date.send_keys(out_of_min_range_date)
    displayed_date = date.get_attribute("value")
    sleep(2)
    print(displayed_date, out_of_min_range_date)
    if displayed_date == out_of_min_range_date:
        return False
    else:
        return True


def enter_incorrect_max_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    date = driver_instance.find_element_by_xpath(date_input)
    out_of_max_range_date = '01-01-2021'
    date.send_keys(out_of_max_range_date)
    displayed_date = date.get_attribute("value")
    sleep(2)
    print(displayed_date, out_of_max_range_date)

    if displayed_date == out_of_max_range_date:
        return False
    else:
        return True

# Testing pseudoelement calendar
def pick_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_input)
    # date_input = driver_instance.find_element_by_xpath(date_input)
    calendar = driver_instance.find_element_by_xpath(cal)
    calendar.click()
    sleep(5)


# Pytania:
# Co jesli kalendarz przyjmuje zle wartosci liczbowe, np. 31.99
# Jak lepiej przetestowac min i max - w wersji ktora mam kalendarz wybiera najblizsza podobna date, czy ten test ma sens?

