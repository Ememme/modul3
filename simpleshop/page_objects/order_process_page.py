import time

from selenium.webdriver.support.select import Select

from simpleshop.tests.data_generator import *
from simpleshop.tests.support_functions import *

name = 'billing_first_name'
lastname = 'billing_last_name'
dropdown_country = 'billing_country'
street = 'billing_address_1'
postcode = 'billing_postcode'
city = 'billing_city'
phone = 'billing_phone'
email = 'billing_email'
place_order_button = 'place_order'

valid_postcode = '00-123'
invalid_postcode = 'abc'

total_order ='//*[@id="order_review"]/table/tfoot/tr[4]/td/strong/span/bdi'


def form_add_valid_name(driver_instance):
    elem = driver_instance.find_element_by_id(name)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_invalid_name(driver_instance):
    elem = driver_instance.find_element_by_id(name)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_valid_lastname(driver_instance):
    elem = driver_instance.find_element_by_id(lastname)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_invalid_lastname(driver_instance):
    elem = driver_instance.find_element_by_id(lastname)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdown_country))
    wait_for_visibility_of_element(driver_instance, dropdown_country)
    elem_list.select_by_index(1)


def form_add_valid_street(driver_instance):
    elem = driver_instance.find_element_by_id(street)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_invalid_street(driver_instance):
    elem = driver_instance.find_element_by_id(street)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_valid_city(driver_instance):
    elem = driver_instance.find_element_by_id(city)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_city(driver_instance):
    elem = driver_instance.find_element_by_id(city)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_valid_postcode(driver_instance):
    elem = driver_instance.find_element_by_id(postcode)
    elem.send_keys(valid_postcode)


def form_add_wrong_postcode(driver_instance):
    elem = driver_instance.find_element_by_id(postcode)
    elem.send_keys(invalid_postcode)


def form_add_valid_phone(driver_instance):
    elem = driver_instance.find_element_by_id(phone)
    elem.send_keys(DataGenerator.generateProperMobileNumber(DataGenerator()))


def form_add_wrong_phone(driver_instance):
    elem = driver_instance.find_element_by_id(phone)
    elem.send_keys(DataGenerator.generateWrongMobileNumber(DataGenerator()))


def form_add_valid_email(driver_instance):
    elem = driver_instance.find_element_by_id(email)
    elem.send_keys(DataGenerator.generateProperEmail())


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element_by_id(email)
    elem.send_keys(DataGenerator.generateWrongEmail())


def fill_all_valid_form_areas(driver_instance):
    form_add_valid_name(driver_instance)
    form_add_valid_lastname(driver_instance)
    get_first_dropdown_value(driver_instance)
    form_add_valid_street(driver_instance)
    form_add_valid_city(driver_instance)
    form_add_valid_postcode(driver_instance)
    form_add_valid_phone(driver_instance)
    form_add_valid_email(driver_instance)


def submit_order(driver_instance):
    wait_for_visibility_of_element(driver_instance, place_order_button)
    time.sleep(10)
    elem = driver_instance.find_element_by_id(place_order_button)
    elem.click()


def total_price(driver_instance):
    wait_for_visibility_of_element(driver_instance, total_order)
    elem = driver_instance.find_element_by_xpath(total_order)
    print(elem.text)
    return elem.text
