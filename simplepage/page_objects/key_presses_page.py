from simplepage.tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

key_presses_tab = '#keypresses-header'
keypress_input = '#target'
keypress_result = '#keyPressResult'

numbers_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
letters_dict = {'a': 'A',
                'b': 'B',
                'c': 'C',
                'd': 'D',
                'e': 'E',
                'f': 'F',
                'g': 'G',
                'h': 'H',
                'i': 'I',
                'j': 'J',
                'k': 'K',
                'l': 'L',
                'm': 'M',
                'n': 'N',
                'o': 'O',
                'p': 'P',
                'q': 'Q',
                'r': 'R',
                's': 'S',
                't': 'T',
                'u': 'U',
                'w': 'W',
                'x': 'X',
                'y': 'Y',
                'z': 'Z'
                }

# Based on: https://www.selenium.dev/selenium/docs/api/py/_modules/selenium/webdriver/common/keys.html#Keys
special_keys_dict = {
    'ENTER': Keys.ENTER,
    'ESC': Keys.ESCAPE,
    'LEFT_SHIFT': Keys.LEFT_SHIFT,
    'RIGHT_SHIFT': Keys.SHIFT,
    'TAB': Keys.TAB,
    'CONTROL': Keys.CONTROL,
    'OPTION_LEFT': Keys.LEFT_ALT,
    'OPTION_RIGHT': Keys.ALT,
    'COMMAND_LEFT': Keys.LEFT_CONTROL,
    'COMMAND_RIGHT': Keys.CONTROL,
    'ARROW_LEFT': Keys.ARROW_LEFT,
    'ARROW_RIGHT': Keys.ARROW_RIGHT,
    'ARROW_UP': Keys.ARROW_UP,
    'ARROW_DOWN': Keys.ARROW_DOWN,
    'SPACE': Keys.SPACE,
    'BACKSPACE': Keys.BACKSPACE,
    'BACK_SPACe': Keys.BACK_SPACE,
    'QUOTE': "'",
    'SEMICOLON_K': Keys.SEMICOLON,
    ']': ']',
    '[': '[',
    'BACK_QUOTE': '`',
    'SLASH': '/',
    'BACKSLASH': '\\',
    'PERIOD': '.',
    'COMMA': ',',
    'EQUALS_K': Keys.EQUALS,
    'EQUALS': '=',
    'SUBTRACT_K': Keys.SUBTRACT,
    'SUBTRACT': '-',
    'ADD_K': Keys.ADD,
    'ADD': '+',
    'SEMICOLON': ';'
}


def click_key_presses_tab(driver_instance):
    tab = driver_instance.find_element_by_css_selector(key_presses_tab)
    tab.click()
    sleep(2)


def is_key_presses_tab_visible(driver_instance):
    wait_for_visibility_of_element_ID(driver_instance, keypress_input)
    content = driver_instance.find_element_by_css_selector(keypress_result)
    return content.is_displayed()


def send_numbers(driver_instance):
    key_input = driver_instance.find_element_by_css_selector(keypress_input)
    result = driver_instance.find_element_by_css_selector(keypress_result)

    errors = []

    for key, value in numbers_dict.items():
        key_input.send_keys(value)
        sleep(.5)
        # print(value, result.get_attribute('textContent'))

        if str(value) not in result.get_attribute('textContent'):
            errors.append([key, result.get_attribute('textContent')])

    if len(errors) == 0:
        return True
    else:
        return False


def send_letters(driver_instance):
    key_input = driver_instance.find_element_by_css_selector(keypress_input)
    result = driver_instance.find_element_by_css_selector(keypress_result)

    errors = []
    for key, value in letters_dict.items():
        key_input.send_keys(value)
        sleep(.1)
        printed = result.get_attribute('textContent').split("You entered:", 1)[-1]
        print(printed)
        if str(value) not in printed:
            errors.append([key, result.get_attribute('textContent')])

    if len(errors) == 0:
        return True
    else:
        return False


def send_special_keys(driver_instance):
    key_input = driver_instance.find_element_by_css_selector(keypress_input)
    result = driver_instance.find_element_by_css_selector(keypress_result)
    errors = []

    for key, value in special_keys_dict.items():
        key_input.send_keys(value)
        sleep(.2)
        printed = result.get_attribute('textContent').split("You entered:", 1)[-1]

        if value not in printed and len(printed) == 1:
            errors.append([key, result.get_attribute('textContent')])

    print(errors)
    if len(errors) == 0:
        return True
    else:
        return False
