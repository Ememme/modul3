# Napisz skrypt, który:
# - wejdzie na stronę fabrykatestow.pl
# - kliknie na zakladke kurs TAPS
# - przeskroluje do 'Kim jest instruktor'
# - zrobi screenshot
import time
from selenium import webdriver

# Setting up driver
driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://fabrykatestow.pl/'

driver.get(url)
# Finding courses tab:
# courses = driver.find_element_by_xpath('//*[@id="menu-item-622"]/a')
courses_tab = driver.find_element_by_partial_link_text('KURSY')
courses_tab.click()

# Finding TAPS course:
courses_all = driver.find_elements_by_link_text('STRONA KURSU')
taps = courses_all[0]
taps.click()
time.sleep(1)
taps_about = driver.find_element_by_css_selector('[data-id="71f1973e"]')
driver.execute_script("arguments[0].scrollIntoView(true);", taps_about)

# Getting data about image in TAPS teacher section
img = taps_about.find_element_by_tag_name('img')
name = img.get_attribute('src')
filename = name.split("/")[-1]
# Saving screenshot as file
driver.save_screenshot(filename)
driver.quit()
