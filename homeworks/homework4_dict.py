def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")



    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        dict_choice = {
            '1': add(num1, num2),
            '2': subtract(num1, num2),
            '3': multiply(num1, num2),
            '4': divide(num1, num2)
        }

        print(dict_choice[choice])
        break

else:
        print("Błędna wartość, podaj poprawną")