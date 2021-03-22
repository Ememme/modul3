from selenium import webdriver
from requests import api
import time

# WEBDRIVER:
driver = webdriver.Chrome()
driver.get('https://fabrykatestow.pl')
driver.close()


# TERMINAL
print('hello Magdalena')
req = api.get('https://fabrykatestow.pl')
time.sleep(5)
print(req.status_code)
time.sleep(5)
print(req.headers['content-type'])
time.sleep(5)
print(req.encoding)
time.sleep(2)
print(req.json)

