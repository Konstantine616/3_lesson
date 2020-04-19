# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(name, sec_name, year, city, phone, email):
    return f'{sec_name} {name} {year} года рождения, проживает в городе {city}, номер телефона: {phone}, email: {email}'


print(user_data(name='Игорь', sec_name='Иванов', year=1980, city='Москва', phone=+79003210078, email='email@mail.com'))
