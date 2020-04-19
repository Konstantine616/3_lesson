# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


while True:
    x = input('Введите число:\n')
    if x.isdigit():
        x = int(x)
        break
    else:
        print('Ошибка ввода.')

while True:
    y = input('Введите число:\n')
    if y.isdigit():
        y = int(y)
        break
    else:
        print('Ошибка ввода.')


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Нельзя делить на ноль.')


print(division(x, y))
