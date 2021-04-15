user_name = input('What is your name?:   ')
user_last = input('What is your last name?:   ')

userdata = (user_name, user_last)
print(userdata)


def reverse(string):
    return string[::-1]


print(reverse(user_name), reverse(user_last))


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")

    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(5,0)
divide(10,2)
