# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_fuck(a, b, c):
    x = sorted([a, b, c])
    return x[1] + x[2]


print(my_fuck(1, 2, 2))