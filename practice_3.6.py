# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(str_el):
    if str_el.islower():
        return str_el.title()
    else:
        print('Строка должна состоять из символов в нижнем регистре.')


def str_func(string):
    string = string.split()
    for el in string:
        if el >= 'a' and el <= 'z':
            string[string.index(el)] = int_func(el)
        print(string)
    return ' '.join(string)


print(str_func('text text 2 3 # text'))
