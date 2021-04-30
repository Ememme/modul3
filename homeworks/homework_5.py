import requests
import time
import json
import csv
from datetime import datetime
from params import api as API_KEY

url = 'http://data.fixer.io/api/latest'


def request_API_data(url):
    try:
        r = requests.get(url, params=API_KEY)
        r_elapsed_time = r.elapsed.total_seconds()
        r_hour = r.headers['date']
        response_data = json.loads(r.text)
        return [response_data, r_elapsed_time, r_hour]
    except requests.exceptions.Timeout:
        print_timeout_error_message()


def print_timeout_error_message():
    print('Brak połączenia z serwisem')


def return_currency_data(currency):
    data = request_API_data(url)
    if data:
        currency_date = data[0]['date']
        currency_rate = data[0]['rates'][currency]
        request_time = data[1]
        request_date = data[2]
        formatted_date = format_time(request_date)
        currency_info = [currency_date, currency_rate, request_time, formatted_date]
        return currency_info
    else:
        print_timeout_error_message()


def format_time(str):
    request_time = str
    time_format = "%a, %d %b %Y %H:%M:%S %Z"
    formatted_time = datetime.strptime(request_time, time_format)
    return formatted_time


def write_csv():
    with open('currency.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([info])


# def get_PLN_rate():
sample = 10

while sample != 0:
    sample = sample - 1
    info = return_currency_data('PLN')
    print(info)

    write_csv()
    date = f"{info[0]}"
    rate_PLN = f"{info[1]}"
    req_date = f"{info[3]}"
    req_time = f"{info[2]}"

    #
    print(f'''
    -----------------------------------------
    Kurs EUR do PLN z dnia {date} wynosi {rate_PLN}
    Zapytanie z dnia {req_date}
    Czas trwania zapytania wyniósł {req_time} s.
        -----------------------------------------''')

    time.sleep(5)
