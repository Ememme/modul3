import requests
import time
import json
import csv

from params import api as API_KEY

url = 'http://data.fixer.io/api/latest'

def request_API_data(url):
    try:
        r = requests.get(url, params=API_KEY)
        r_time = r.elapsed.total_seconds()
        response_data = json.loads(r.text)
        return [response_data, r_time]
    except requests.exceptions.Timeout:
        print_connection_error_message()

def print_connection_error_message():
    print('Brak połączenia z serwisem')

def return_currency_data(currency):
    data = request_API_data(url)
    if data:
        # print(data)
        date = data[0]['date']
        currency = data[0]['rates'][currency]
        request_time = data[1]
        info = [currency, request_time, date]
        # print(info)
        return info


def write_csv():
    with open('currency.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([info])

sample = 10

while sample != 0:
    sample = sample - 1
    info = return_currency_data('PLN')
    print(info)

    rate_PLN = f"{info[0]}"
    req_time = f"{info[1]}"
    date = f"{info[2]}"

    write_csv()
    print(f'''
    -----------------------------------------
    Kurs EUR do PLN z dnia {date} wynosi {rate_PLN}
    Czas trwania zapytania wyniósł {req_time} s.
    -----------------------------------------''')

    time.sleep(5)
